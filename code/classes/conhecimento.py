class Conhecimento():


	def __init__(self, tipo_conhecimento, valor_inicial_conhecimento, n_ru):

		self.tipo_conhecimento = tipo_conhecimento # 
		self.n_ru = n_ru # numero de filosofos ou militares
		self.lista_conhecimento = [valor_inicial_conhecimento] # valor inicial do conhecimento eh o valor inicial da lista, mesmo valor de pessoas que "ajudaram no conhecimento"
		

	# usa as pessoas para desenvolver o conhecimento, dependendo do nivel para o tipo de conhecimento, o desenvolvimento pode ficar mais rapido ou mais lento
	def DesenvolverConhecimento(self, pessoas, taxa_desenvolvimento_anual, player):

		# se conhecimento ainda nao foi totalmente desenvolvido
		if not (self.lista_conhecimento[-1] == 0):
			# loop de 1 ate a taxa de desenvolvimente + 1 -> id das pessoas
			x = 0
			# n_ru pois so de trabalhar no desenvolvimento do conhecimento ele ja eh atualizado
			# n_desenvolvimento = self.n_ru
			n_desenvolvimento = 0

			# print("pessoas----------")
			# print(pessoas)
			# print("pessoas----------")

			for idp, pessoa in pessoas.items():
				
				# 1 se a pessoa nao for da mesma ideologia do conhecimento, 2 se for
				n_desenvolvimento_atual = 1

				if pessoa.Ideologia() == "filosofo" and self.tipo_conhecimento == "f":
					n_desenvolvimento_atual = 2
					
				if pessoa.Ideologia() == "militar" and self.tipo_conhecimento == "m":
					n_desenvolvimento_atual = 2

				# quantidade para desenvolver conhecimento
				n_desenvolvimento = n_desenvolvimento + n_desenvolvimento_atual

				# quando X for igual taxa de desenvolvimento devo sair
				# da pra salvar o X e continuar de onde parou na proxima, chegando no maximo eu preciso voltar pro 0, nao vou fazer agora por preguica
				x = x + 1
				if x == taxa_desenvolvimento_anual:
					break

			# se o n_desen for maior que a diferenca entre o ultimo elemento da lista e 0
			# n_desen fica como a diferenca 
			if (self.lista_conhecimento[-1] - n_desenvolvimento) < 0:
				n_desenvolvimento = abs(0 - self.lista_conhecimento[-1])

			# n_desen = diferenca entre o ultimo elemento da lista e n_desen antigo
			n_desenvolvimento = self.lista_conhecimento[-1] - n_desenvolvimento
			self.lista_conhecimento.append(n_desenvolvimento)

			# se desenvolveu tudo, player ganha numero de pontos igual ao valor inicial do conhecimento (dificiuldade do memso)
			if n_desenvolvimento == 0:
				player.AddPontos(self.lista_conhecimento[0])

	def ExibirDados(self):
		print("Tipo do conhecimento: {}".format(self.tipo_conhecimento))
		print("Quantidade de RU: {}".format(self.n_ru))
		print("Representacao do conhecimento: {}".format(self.lista_conhecimento))

		
		


