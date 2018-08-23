from .conhecimento import Conhecimento

class Player():
	# A classe player tem tudo o que player TEM e PODE FAZER

	def __init__(self, nome, n_pessoas, filosofos=5, militares=5):
		self.nome = nome # nome player
		self.n_filosofo = filosofos # qtd de filosofos na nacao
		self.n_militar = militares # qtd de militares na nacao
		self.n_pessoa = n_pessoas # qtd de pessoas na nacao

		self.conhecimentos = []
		self.pessoas = None # pessoas da nacao, dict

		self.taxa_desenvolvimento_anual = self.n_pessoa / 2 # 2 anos necessarios para desenvolver um conhecimento envolvendo toda nacao, podendo ser mais rapido se o conhecimento for igual as ideologias das pessoas

		self.pontos = 0

		self.idp_pessoas_remover = []
		self.idp_pessoas_add = []
		self.pessoas_add = []

	def RemovePessoa(self, idp):
		self.idp_pessoas_remover.append(idp)
		# del self.pessoas[idp]
		# self.n_pessoa = self.n_pessoa - 1

	def AddPessoa(self, idp, pessoa):
		self.idp_pessoas_add.append(idp)
		self.pessoas_add.append(pessoa)
		
		# self.pessoas[idp] = pessoa
		# self.n_pessoa = self.n_pessoa + 1
		# self.taxa_desenvolvimento_anual = self.n_pessoa / 10 # 10 anos necessarios para desenvolver um conhecimento envolvendo toda nacao, podendo ser mais rapido se o conhecimento for igual as ideologias das pessoas
		# self.pontos = self.pontos + 1 # 1 ponto por conquistar uma pessoa

	def RemovePessoa2(self, idp):
		del self.pessoas[idp]
		self.n_pessoa = self.n_pessoa - 1

	def AddPessoa2(self, idp, pessoa):
		self.pessoas[idp] = pessoa
		self.n_pessoa = self.n_pessoa + 1
		self.taxa_desenvolvimento_anual = self.n_pessoa / 10 # 10 anos necessarios para desenvolver um conhecimento envolvendo toda nacao, podendo ser mais rapido se o conhecimento for igual as ideologias das pessoas
		self.pontos = self.pontos + 1 # 1 ponto por conquistar uma pessoa

	def AddPessoas(self, pessoasDict):
		self.pessoas = pessoasDict


	def AddPontos(self, valor):
		self.pontos = self.pontos + valor

	# gera um conhecimento novo -> n_ru: numero de filosofos ou militares desenvolvendo o conhecimento
	def CriarConhecimento(self, tipo_conhecimento, n_pessoas_conhecimento, n_ru): 

		# se tipo_conhecimento for diferente de F (filosofo) e de M (militar) -> tentar arrumar
		if tipo_conhecimento != "f" and tipo_conhecimento != "m":
			tipo_conhecimento = input("Digite f (filosofo) ou m (militar) para o tipo do conhecimento")

		# checar numero de pessoas, se for maior que pessoas na nacao, usa o numero total de pessoas na nacao
		if n_pessoas_conhecimento > self.n_pessoa:
			n_pessoas_conhecimento = self.n_pessoa

		# checar numero de RU, se for maior que RU na nacao, usa o numero total de RU na nacao
		if tipo_conhecimento == "f" and n_ru > self.n_filosofo:
			n_ru = self.n_filosofo
		if tipo_conhecimento == "m" and n_ru > self.n_militar:
			n_ru = self.n_militar

		c = Conhecimento(tipo_conhecimento, n_pessoas_conhecimento, n_ru)
		self.conhecimentos.append(c) # conhecimento criado e adicionado


	def DesenvolverConhecimento(self, n_conhecimento):
		
		# se numero do conhecimento nao existe, desenvolve o primeiro da lista
		if n_conhecimento < 0 or n_conhecimento >= len(self.conhecimentos):
			n_conhecimento = 0

		# conhecimento que deve ser desenvolvido
		conhecimento = self.conhecimentos[n_conhecimento] 

		# print("pessoas----------")
		# type(self.pessoas)
		# print("pessoas----------")

		conhecimento.DesenvolverConhecimento(self.pessoas, self.taxa_desenvolvimento_anual, self)

		# para a segunda versao do jogo
		# for idp, pessoa in self.pessoas.items():
		# 	pessoa.ConversarComConhecidos()

		# for idp in self.idp_pessoas_remover:
		# 	self.RemovePessoa2(idp)

		# for i in range(0, len(self.idp_pessoas_add)):
		# 	self.AddPessoa2(self.idp_pessoas_add[i], self.pessoas_add[i])

		# pode ser melhorado

	def ExibirDados(self):
		print("Jogador {} -------- pontos: {}".format(self.nome, self.pontos))
		print("numero de filosofos: {} - numero de militares: {}".format(self.n_filosofo, self.n_militar))
		print("numero de pessoas: {}".format(self.n_pessoa))
		print("taxa de desenvolvimento anual: {}".format(self.taxa_desenvolvimento_anual))
		print("Conhecimentos: {}".format(len(self.conhecimentos)))

		for conhecimento in self.conhecimentos:
			conhecimento.ExibirDados()

		print("__________________")


		