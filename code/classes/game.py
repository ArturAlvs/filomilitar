from .player import Player
from .pessoa import Pessoa
from random import randint


class Game():
	"""docstring for Game"""

	def __init__(self, p0, p1, n_inicial_pessoas):

		self.p0 = p0
		self.p1 = p1
		self.n_inicial_pessoas = n_inicial_pessoas
		self.n_pessoas = n_inicial_pessoas # caso pessoas morram, pessoas nao podem morrer por enquanto, mas vou deixar aqui pq vai que um dia pode, e pessoas devem morrer as vezes pro equilibrio de toda energia universal, flw vlw

		self.ano = 0

		# 0 para p0 e 1 para p1
		self.player_turno = 0 


	def ExibirDados(self):
		print("________________________")
		print("Ano {}".format(self.ano))
		print("________________________")

		self.p0.ExibirDados()
		self.p1.ExibirDados()

	# vai ficar pra segunda versao do jogo
	def TrocaDeNacao(self, de, para, idp, pessoa):
		
		# da nacao 0 para nacao 1 (nacao = player)
		if de == 0 and para == 1:
			if self.p0.n_pessoa > 0:
				# tirar pessoa da nacao 0
				self.p0.RemovePessoa(idp)
				# add pessoa na nacao 1
				self.p1.AddPessoa(idp, pessoa)
			else:
				print("{} ganhou o jogo".format(self.p1.nome))
				self.player_turno = 666

		if de == 1 and para == 0:
			if self.p1.n_pessoa > 0:
				# tirar pessoa da nacao 0
				self.p0.AddPessoa(idp, pessoa)
				# add pessoa na nacao 1
				self.p1.RemovePessoa(idp)
			else:
				print("{} ganhou o jogo".format(self.p0.nome))
				self.player_turno = 666
			

	# def CriarPlayer(self, player, nome, pessoas, filosofos, militares ):
	# 	# Player 0
	# 	if player == 0:
	# 		self.p0 = Player(nome, pessoas, filosofos, militares)

	# 	# Player 1
	# 	if player == 1:
	# 		self.p1 = Player(nome, pessoas, filosofos, militares)

	
	def CriarPessoa(self, idp, nacao, game):

		sexo = randint(0, 1)
		if sexo == 0:
			sexo = "masculino"
		else:
			sexo = "feminino"

		# nivel filosofo eh random e nivel militar eh o complemento para 100
		nivel_filosofo = randint(0,100)	
		nivel_militar = 100 - nivel_filosofo

		p = Pessoa(idp, sexo, nivel_filosofo, nivel_militar, nacao, game)

		return p

	def GerarConhecidos(self, idp, n_pessoas_por_nacao):
		conhecidos = []

		n_conhecidos = randint(2,5)

		for x in range(0,n_conhecidos):
			
			# gera o id do conhecido, se for o mesmo id da pessoa, gero um novo
			id_do_conhecido = randint(1, n_pessoas_por_nacao)
			while id_do_conhecido == idp:
				id_do_conhecido = randint(1, n_pessoas_por_nacao)

			# Se for do player 1, faz id ficar negativo
			if idp < 0:
				id_do_conhecido = id_do_conhecido * (-1)

			conhecidos.append(id_do_conhecido) # adicionando o id do conhecido na lista

		# adicionando um conhecido de outra nacao (do outro player)
		id_do_conhecido = randint(1, n_pessoas_por_nacao)
		if idp > 0:
			id_do_conhecido = id_do_conhecido * (-1)

		conhecidos.append(id_do_conhecido)
		

		return conhecidos
				

	def CriarPessoas(self):
		
		# se tem numero impar de pessoas, adiona mais um
		if self.n_inicial_pessoas % 2 != 0:
			self.n_inicial_pessoas = self.n_inicial_pessoas + 1 


		n_pessoas_por_nacao = int(self.n_inicial_pessoas / 2) # numero de pessoas por nacao

		# id das pessoas e dicionario, _0 = player 1 e _1 = player 2
		pessoas_0 = {}
		pessoas_1 = {}

		id_pessoa_0 = 1
		id_pessoa_1 = -1
		for x in range(0, n_pessoas_por_nacao):
			
			p0 = self.CriarPessoa(id_pessoa_0, 0, self) # cria a pessoa
			pessoas_0[id_pessoa_0] = p0 # adiciona pessoa na lista com key = o id

			p1 = self.CriarPessoa(id_pessoa_1, 1, self) # cria a pessoa
			pessoas_1[id_pessoa_1] = p1 # adiciona pessoa na lista com key = o id

			# criando lista de conhecidos
			conhecidos_0 = self.GerarConhecidos(id_pessoa_0, n_pessoas_por_nacao)
			conhecidos_1 = self.GerarConhecidos(id_pessoa_1, n_pessoas_por_nacao)

			# Adicionando os conhecidos nas pessoas
			# pra ficar simples, nao to fazendo: se pessoa A conhece pessoa B, pessoa B conhece pessoa A. 
			# posso fazer depois, fazer um grafo de toda a populacao
			p0.AdicionarConhecidos(conhecidos_0)
			p1.AdicionarConhecidos(conhecidos_1)

			
			# modificando o id das proximas pessoas
			id_pessoa_0 = id_pessoa_0 + 1
			id_pessoa_1 = id_pessoa_1 - 1

		# adicionando as pessoas nos players
		
		self.p0.AddPessoas(pessoas_0)
		self.p1.AddPessoas(pessoas_1)

		# print(self.p0.pessoas)
		# print(self.p1.pessoas)

		# print("pessoas criadas")
		# print(pessoas_0)

	

	def RealizarAcao(self, acao, player, tipo_conhecimento=None, n_pessoas_conhecimento=None, n_ru=None, n_conhecimento=None):
		
		# Gerar Conhecimento
		if acao == "gc":
			player.CriarConhecimento(tipo_conhecimento, n_pessoas_conhecimento, n_ru)

		elif acao == "dc": # desenvolver conhecimento
			player.DesenvolverConhecimento(n_conhecimento)

	
	def StartGame(self):
		self.CriarPessoas()

	def TurnoJogar(self):

		# controlador de turnos
		if self.player_turno == 0:
			player = self.p0
			self.player_turno = 1
		elif self.player_turno == 1:
			player = self.p1
			self.player_turno = 0
			# Finalizando o turno aqui pois devo esperar os dois jogadores jogar
			self.FinalizarTurno()
		else:
			# nao tem mais turno
			print("Jogo finalizado, por favor, feche a conexao :)")
			inp = input("Tchau.")


		print("{} turno".format(player.nome))
		print("Acoes:")
		print("gc = Gerar conhecimento, logo apos voce deve escolher o tipo do conhecimento, numero de pessoas envolvidas no conhecimento e o numero de recurso especializado utilizado no conhecimento")
		print("dc = Desenvolve conhecimento, logo apos voce deve escolher o conhecimento desejado")
		comando = input("Escolha sua acao ")

		while comando != "gc" and comando != "dc":
			# print(comando)
			comando = input("Escolha sua acao: [gc] [dc] ")

		if comando == "dc" and len(player.conhecimentos) <= 0:
			comando = "gc" # :)
				
		# se for pra DESENVOLVER CONHECIMENTO, pede os outros dados		
		if comando == "dc":
			n_conhecimento = input("Escolha o numero do conhecimento: min 0, max {} ".format(len(player.conhecimentos) - 1))
			n_conhecimento = int(n_conhecimento)

			# convertendo para passar para as funcoes
			while n_conhecimento < 0 or n_conhecimento > len(player.conhecimentos) - 1:
				n_conhecimento = input("Escolha o numero do conhecimento: min 0, max {} ".format(len(player.conhecimentos) - 1))
				n_conhecimento = int(n_conhecimento)

				
			# n_conhecimento = int(n_conhecimento)
			self.RealizarAcao(comando, player, n_conhecimento=n_conhecimento)

		# se for pra GERAR CONHECIMENTO, pede os outros dados
		elif comando == "gc":
			tipo_conhecimento = input("Escolha o tipo de conhecimento: [f] para filosofo ou [m] para militar ")
			while tipo_conhecimento != "f" and tipo_conhecimento != "m":
				tipo_conhecimento = input("Escolha o tipo de conhecimento: [f] para filosofo ou [m] para militar ")

			# poderia estar melhor, mas o tempo grita
			n_pessoas_conhecimento = input("Escolha qual a dificuldade do seu conhecimento, numero de pessoas envolvidas: min 1, max {} ".format(player.n_pessoa))
			n_pessoas_conhecimento = int(n_pessoas_conhecimento)
			while n_pessoas_conhecimento < 1 or n_pessoas_conhecimento > player.n_pessoa:
				n_pessoas_conhecimento = input("Escolha qual a dificuldade do seu conhecimento, numero de pessoas envolvidas: min 1, max {} ".format(player.n_pessoa))
				n_pessoas_conhecimento = int(n_pessoas_conhecimento)
				
			n_ru = input("Escolha quantos especialistas devem trabalhar no conhecimento: min 0, max {} ou {} ".format(player.n_filosofo, player.n_militar))
			n_ru = int(n_ru)
			while n_ru < 0 or (tipo_conhecimento == "f" and n_ru > player.n_filosofo) or (tipo_conhecimento == "m" and n_ru > player.n_militar):
				n_ru = input("Escolha quantos especialistas devem trabalhar no conhecimento: min 0, max {} ou {} ".format(player.n_filosofo, player.n_militar))
				n_ru = int(n_ru)
				

			# convertendo para passar para as funcoes
			# n_pessoas_conhecimento = int(n_pessoas_conhecimento)
			# n_ru = int(n_ru)
			self.RealizarAcao(comando, player, tipo_conhecimento=tipo_conhecimento, n_pessoas_conhecimento=n_pessoas_conhecimento, n_ru=n_ru)

		print("--------------TURNO FINALIZADO--------------------")


		


		

	def FinalizarTurno(self):
		# TODO as pessoas tem que conversar
		self.ano = self.ano + 1

