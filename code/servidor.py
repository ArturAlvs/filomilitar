
# Falta mandar para os espectadores
# TODO
# Relatorio
# melhorar jogo
# Pessoas conversar


host = "127.0.0.1"		# Set the server address to variable host
port = 4475			# Sets the variable port to 4444
from socket import *	# Imports socket module
from threading import Thread
import pickle
from classes.game import *
from classes.player import Player

import sys



players = []
espectadores = []

p0_nome = None
p1_nome = None


class Th(Thread):

	def __init__ (self, m_socket):
		Thread.__init__(self)
		self.m_socket = m_socket

		# criar salas depois
		# self.salas = {}

		self.players = []
		self.espectadores = []

	def run(self):
		while True:
			# Accepts incoming request from client and returns
			# socket and address to variables client and Informations
			client, Informations = self.m_socket.accept()
			
			tipo = client.recv(1024) # mudar valor depois
			# tipo = pickle.loads(b"".join(tipo))
			tipo = tipo.decode()

			print("{} conectado [ {} ]".format(tipo, Informations))

			if tipo == "player" and len(self.players) < 2:
				self.players.append(client)
				
			elif tipo == "espectador":
				self.espectadores.append(client)


			# print(self.players)
			# print(self.espectadores)

		self.m_socket.close()


s = socket(AF_INET, SOCK_STREAM)

s.bind((host,port))	# Binds the socket. Note that the input to 
				    # the bind function is a tuple
s.listen(3)			# Sets socket to listening state with a  queue
				    # of 1 connection
print ("Listening for connections.. ")


server_thread = Th(s)
server_thread.start()

# pega os nomes dos jogadores
def PlayersNomes(players):

	# pergunta_nome = "Escolha um nome.".encode()
	pergunta_nome = pickle.dumps("Escolha um nome.")

	players[0].send(pergunta_nome)
	p0_nome = players[0].recv(1024)
	# p0_nome = p0_nome.decode()
	p0_nome = pickle.loads(p0_nome)

	players[1].send(pergunta_nome)
	p1_nome = players[1].recv(1024)
	# p1_nome = p1_nome.decode()
	p1_nome = pickle.loads(p1_nome)


	return p0_nome, p1_nome

# instancia os objetos para o jogo iniciar
def GameStart(players):
	
	# if len(players) != 2:
	# 	return

	p0_nome, p1_nome = PlayersNomes(players)

	# Valores que eu coloquei
	n_inicial_pessoas = 20
	n_pessoas_por_nacao = n_inicial_pessoas / 2

	player_0 = Player(p0_nome, n_pessoas_por_nacao, 5, 5)
	player_1 = Player(p1_nome, n_pessoas_por_nacao, 5, 5)

	jogo = Game(player_0, player_1, n_inicial_pessoas)

	jogo.StartGame()

	return jogo

# envia e espera o jogo do jogador da rodada
def Turno(player, jogo, espectadores_ativos):
	
	jogo_serializado = pickle.dumps(jogo)
	player.sendall(jogo_serializado)

	for espectador in espectadores_ativos:
		espectador.sendall(jogo_serializado)

	jogo_recebido = player.recv(4096)

	# chunks = []
	# bytes_recd = 0
	# MSGLEN = 4096
	# while bytes_recd < MSGLEN:
	# 	chunk = player.recv(min(MSGLEN - bytes_recd, 4096))
	# 	if chunk == b'':
	# 		raise RuntimeError("socket connection broken")
	# 	chunks.append(chunk)
	# 	bytes_recd = bytes_recd + len(chunk)
	# jogo_recebido = b''.join(chunks)

	jogo_recebido = pickle.loads(jogo_recebido)
	print(jogo_recebido)

	

	return jogo_recebido

# nao deveria estar aqui, mas to sem tempo
# se houver vitoria retorna True, caso contrario retorna False
def ChecarVitoria(jogo, players, espectadores):
	# checa se alguem ganhou, fez 20 pontos

	if jogo.p0.pontos >= 50:
		jogo.player_turno = 666
		print("{} ganhou o jogo.".format(jogo.p0.nome))
		for espectador in espectadores:
			espectador.sendall(pickle.dumps("Jogador com mais pontos ganhou o jogo."))
		players[0].sendall(pickle.dumps("vitoria"))
		players[1].sendall(pickle.dumps("derrota"))
		return True
	elif jogo.p1.pontos >= 50:
		jogo.player_turno = 666
		print("{} ganhou o jogo.".format(jogo.p1.nome))
		for espectador in espectadores:
			espectador.sendall(pickle.dumps("Jogador com mais pontos ganhou o jogo."))
		players[0].sendall(pickle.dumps("derrota"))
		players[1].sendall(pickle.dumps("vitoria"))
		return True

	return False


# objeto de jogo
jogo = None

# loop do jogo
while True:

	players = server_thread.players
	espectadores = server_thread.espectadores

	# se jogo nao comecou
	if jogo == None and len(players) == 2:
		jogo = GameStart(players)

	elif jogo != None and len(players) == 2:

		# se alguem ganhou, volta no loop e nao chama nenhum turno, fica dando continue
		if ChecarVitoria(jogo, players, espectadores):
			break

		print("Turno Player 0")

		jogo = Turno(players[0], jogo, espectadores)


		# inp = input("Proximo turno? ")
		print("Turno Player 1")

		jogo = Turno(players[1], jogo, espectadores)


		# inp = input("Proximo turno? ")



s.close()
