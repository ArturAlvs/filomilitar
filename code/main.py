from classes.game import *
from classes.player import Player


p0_nome = "Player0"
p1_nome = "Player1"
n_inicial_pessoas = 1000
n_pessoas_por_nacao = n_inicial_pessoas / 2

player_0 = Player(p0_nome, n_inicial_pessoas, 5, 5)
player_1 = Player(p1_nome, n_inicial_pessoas, 5, 5)

jogo = Game(player_0, player_1, n_inicial_pessoas)

print(player_0)
print(player_1)
print(jogo)

jogo.StartGame()

# Loop do jogo
while True:

	# exibe os dados do jogo
	jogo.ExibirDados()

	# turno do jogador p0
	jogo.TurnoJogar()
	
	# turno do jogador p1
	jogo.TurnoJogar()

	jogo.FinalizarTurno()


	# print("{} turno".format(player_0.nome))
	# print("Acoes:")
	# print("gc = Gerar conhecimento, logo apos voce deve escolher o tipo do conhecimento, numero de pessoas envolvidas no conhecimento e o numero de recurso especializado utilizado no conhecimento")
	# print("dc = Desenvolve conhecimento, logo apos voce deve escolher o conhecimento desejado")
	# comando = input("Escolha sua acao ")

	# while comando != "gc" and comando != "dc":
	# 	print(comando)
	# 	comando = input("Escolha sua acao ")
	# 	if comando == "dc" and len(player_0.conhecimentos) == 0:
	# 		comando = input("Voce nao tem nenhum Conhecimento para desenvolver, voce DEVE escolher [gc]")
			

	# if comando == "dc":
	# 	n_conhecimento = input("Escolha o numero do conhecimento: min 0, max {} ".format(len(player_0.conhecimentos) - 1))
	# 	# convertendo para passar para as funcoes
	# 	n_conhecimento = int(n_conhecimento)
	# 	jogo.RealizarAcao(comando, player_0, n_conhecimento=n_conhecimento)

		
	# elif comando == "gc":
	# 	tipo_conhecimento = input("Escolha o tipo de conhecimento: [f] para filosofo ou [m] para militar ")
	# 	n_pessoas_conhecimento = input("Escolha qual a dificuldade do seu conhecimento, numero de pessoas envolvidas: min 1, max {} ".format(player_0.n_pessoa))
	# 	n_ru = input("Escolha quantos especialistas devem trabalhar no conhecimento: min 0, max {} ou {} ".format(player_0.n_filosofo, player_0.n_militar))	
	# 	# convertendo para passar para as funcoes
	# 	n_pessoas_conhecimento = int(n_pessoas_conhecimento)
	# 	n_ru = int(n_ru)
	# 	jogo.RealizarAcao(comando, player_0, tipo_conhecimento=tipo_conhecimento, n_pessoas_conhecimento=n_pessoas_conhecimento, n_ru=n_ru)

	# PLAYER 2 --------------------------------------

	# print("----------------------------------")

	# print("{} turno".format(player_1.nome))
	# print("Acoes:")
	# print("gc = Gerar conhecimento, logo apos voce deve escolher o tipo do conhecimento, numero de pessoas envolvidas no conhecimento e o numero de recurso especializado utilizado no conhecimento")
	# print("dc = Desenvolve conhecimento, logo apos voce deve escolher o conhecimento desejado")
	# comando = input("Escolha sua acao ")

	# while comando != "gc" and comando != "dc":
	# 	print(comando)
	# 	comando = input("Escolha sua acao ")
	# 	if comando == "dc" and len(player_1.conhecimentos) == 0:
	# 		comando = input("Voce nao tem nenhum Conhecimento para desenvolver, voce DEVE escolher [gc]")
			

	# if comando == "dc":
	# 	n_conhecimento = input("Escolha o numero do conhecimento: min 0, max {} ".format(len(player_1.conhecimentos) - 1))
	# 	# convertendo para passar para as funcoes
	# 	n_conhecimento = int(n_conhecimento)
	# 	jogo.RealizarAcao(comando, player_1, n_conhecimento=n_conhecimento)

		
	# elif comando == "gc":
	# 	tipo_conhecimento = input("Escolha o tipo de conhecimento: [f] para filosofo ou [m] para militar ")
	# 	n_pessoas_conhecimento = input("Escolha qual a dificuldade do seu conhecimento, numero de pessoas envolvidas: min 1, max {} ".format(player_1.n_pessoa))
	# 	n_ru = input("Escolha quantos especialistas devem trabalhar no conhecimento: min 0, max {} ou {} ".format(player_1.n_filosofo, player_1.n_militar))	
	# 	# convertendo para passar para as funcoes
	# 	n_pessoas_conhecimento = int(n_pessoas_conhecimento)
	# 	n_ru = int(n_ru)
	# 	jogo.RealizarAcao(comando, player_1, tipo_conhecimento=tipo_conhecimento, n_pessoas_conhecimento=n_pessoas_conhecimento, n_ru=n_ru)





