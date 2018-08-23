from threading import Thread

class Pessoa():
	"""docstring for Pessoa"""

	def __init__(self, id_pessoa, sexo, nivel_filosofo, nivel_militar, nacao, game):
		
		self.id_pessoa = id_pessoa
		self.sexo = sexo
		self.nivel_filosofo = nivel_filosofo
		self.nivel_militar = nivel_militar

		self.game = game

		self.nacao = nacao

		self.conhecidos = None # lista de conhecidos

		self.conhecimentos = None # de inicio as pessoas nao ajudou em nenhum conhecimento ainda


	def AdicionarConhecidos(self, conhecidos):
		self.conhecidos = conhecidos

	def Ideologia(self):
		
		if self.nivel_filosofo >= self.nivel_militar:
			return "filosofo"
		else :
			return "militar"

	def MelhorarFilosofia(self, valor):
		# Se nivel militar ainda existe, tira um e bota em filosofo
		if pA.nivel_militar > 0:
			pA.nivel_filosofo = pA.nivel_filosofo + 1
			pA.nivel_militar = pA.nivel_militar - 1
		if pB.nivel_militar > 0:
			pB.nivel_filosofo = pB.nivel_filosofo + 1
			pB.nivel_militar = pB.nivel_militar - 1


	def Conversa_MesmaNacao_MesmaIdeologia(self, pA, pB):
		
		pA_Ideologia = pA.Ideologia()
		pB_Ideologia = pB.Ideologia()

		# Verificando Ideologia e Nacao
		if pA_Ideologia == pB_Ideologia and pA.nacao == pB.nacao:
			
			if pA_Ideologia == "filosofo":
				
				# Se nivel militar ainda existe, tira um e bota em filosofo
				if pA.nivel_militar > 0:
					pA.nivel_filosofo = pA.nivel_filosofo + 1
					pA.nivel_militar = pA.nivel_militar - 1
				if pB.nivel_militar > 0:
					pB.nivel_filosofo = pB.nivel_filosofo + 1
					pB.nivel_militar = pB.nivel_militar - 1

			if pA_Ideologia == "militar":
				
				# Se nivel filosofo ainda existe, tira um e bota em militar
				if pA.nivel_filosofo > 0:
					pA.nivel_militar = pA.nivel_militar + 1
					pA.nivel_filosofo = pA.nivel_filosofo - 1
				if pB.nivel_filosofo > 0:
					pB.nivel_militar = pB.nivel_militar + 1
					pB.nivel_filosofo = pB.nivel_filosofo - 1


			return True # se foi verdade

		return False # se nao foi verdade :)

	def Conversa_MesmaIdeologia_NacaoDiferente(self, pA, pB):
		
		pA_Ideologia = pA.Ideologia()
		pB_Ideologia = pB.Ideologia()

		# Verificando Ideologia e Nacao
		if pA_Ideologia == pB_Ideologia and pA.nacao != pB.nacao:
			
			if pA_Ideologia == "filosofo":
				
				# Quem for mais "fraco" troca de nacao
				if pA.nivel_filosofo > pB.nivel_filosofo:
					self.game.TrocaDeNacao(pB.nacao, pA.nacao, pB.id_pessoa, pB)
					pB.nacao = pA.nacao
				elif pB.nivel_filosofo > pA.nivel_filosofo:
					self.game.TrocaDeNacao(pA.nacao, pB.nacao, pA.id_pessoa, pA)
					pA.nacao = pB.nacao

			if pA_Ideologia == "militar":
				
				# Quem for mais "fraco" troca de nacao
				if pA.nivel_militar > pB.nivel_militar:
					self.game.TrocaDeNacao(pB.nacao, pA.nacao, pB.id_pessoa, pB)
					pB.nacao = pA.nacao
				elif pB.nivel_militar > pA.nivel_militar:
					self.game.TrocaDeNacao(pA.nacao, pB.nacao, pA.id_pessoa, pA)
					pA.nacao = pB.nacao


			return True # se foi verdade

		return False # se nao foi verdade :)


	def Conversa_IdeologiaDiferente(self, pA, pB):

		pA_Ideologia = pA.Ideologia()
		pB_Ideologia = pB.Ideologia()

		# Verificando Ideologia
		if pA_Ideologia != pB_Ideologia:
			# diferenca entre as ideologias de cada pessoa
			dif_entre_ideologias_pA = abs(pA.nivel_militar - pA.nivel_filosofo)
			dif_entre_ideologias_pB = abs(pB.nivel_militar - pB.nivel_filosofo)

			# Se Dif de A for maior que de B -e> A eh filosofo
			if dif_entre_ideologias_pA > dif_entre_ideologias_pB:
				
				if pA_Ideologia == "filosofo":
				
					# Se nivel militar ainda existe, tira 2 e bota em filosofo
					if pA.nivel_militar > 1:
						pA.nivel_filosofo = pA.nivel_filosofo + 2
						pA.nivel_militar = pA.nivel_militar - 2
					if pB.nivel_militar > 1:
						pB.nivel_filosofo = pB.nivel_filosofo + 2
						pB.nivel_militar = pB.nivel_militar - 2

				if pA_Ideologia == "militar":
					# diferenca entre a diferenca das pessoas
					dif_entre_pessoas = abs(dif_entre_ideologias_pA - dif_entre_ideologias_pB)
					
					# esse numero pode mudar, ele que define quao diferente tem que ser pra modificar a ideologia da pessoa (30)
					if dif_entre_pessoas > 30:
						
						# Se nivel filosofo ainda existe, tira um e bota em militar
						if pA.nivel_filosofo > 1:
							pA.nivel_militar = pA.nivel_militar + 2
							pA.nivel_filosofo = pA.nivel_filosofo - 2
						if pB.nivel_filosofo > 1:
							pB.nivel_militar = pB.nivel_militar + 2
							pB.nivel_filosofo = pB.nivel_filosofo - 2
					else :

						# Se nivel militar ainda existe, tira 2 e bota em filosofo
						if pA.nivel_militar > 1:
							pA.nivel_filosofo = pA.nivel_filosofo + 2
							pA.nivel_militar = pA.nivel_militar - 2
						if pB.nivel_militar > 1:
							pB.nivel_filosofo = pB.nivel_filosofo + 2
							pB.nivel_militar = pB.nivel_militar - 2

			

			return True

		return False


	def ConversarComConhecidos(self):
		
		# interando sobre os conhecidos, id dos conhecidos
		for idp in self.conhecidos:

			try:
				# tenta pegar a pessoa do player 0
				pessoaB = self.game.p0.pessoas[idp]
			except Exception as e:
				# tenta pegar a pessoa do player 1
				pessoaB = self.game.p1.pessoas[idp]


			# se sao da mesma nacao
			if self.Conversa_MesmaNacao_MesmaIdeologia(self, pessoaB):
				continue
			elif self.Conversa_MesmaIdeologia_NacaoDiferente(self, pessoaB):
				continue
			elif self.Conversa_IdeologiaDiferente(self, pessoaB):
				continue

		# class Th(Thread):

		# 	def __init__ (self, pessoaB):
		# 		Thread.__init__(self)
		# 		self.pessoaB = pessoaB

		# 	def run(self):

		# 		# se sao da mesma nacao
		# 		if self.Conversa_MesmaNacao_MesmaIdeologia(self, pessoaB):
		# 			ksadgfadskjfsdajkfsad = 2
		# 		elif self.Conversa_MesmaIdeologia_NacaoDiferente(self, pessoaB):
		# 			ksadgfadskjfsdajkfsad = 2
		# 		elif self.Conversa_IdeologiaDiferente(self, pessoaB):
		# 			ksadgfadskjfsdajkfsad = 2

		# # # interando sobre os conhecidos
		# # criando thread para cada conhecido e execuntando as funcoes
		# for x in self.conhecidos:
		# 	thread = Th(x)
		# 	thread.start()
