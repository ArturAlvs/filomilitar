# from classes.s_socket import *

# # host = 192.168.1.4
# host = 'localhost'
# port = 4000

# msg = "cli at"

# msg = msg.encode()

# con = MySocket()

# con.connect(host, port)
# con.mysend(msg)
# response = con.myreceive()

# print(response)




import socket, pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('localhost', 4475))

data = "player".encode()
server.send(data)

jogo = None

while True:
	# inp = input("Msg: ")
	# data = inp
	# data = pickle.dumps(data)
	# server.send(data)
	data = server.recv(4096)
	if not data:
		break
	# data = data.decode()
	data = pickle.loads(data)

	if data == "Escolha um nome.":
		nome = input(data)
		# nome = nome.encode()
		nome = pickle.dumps(nome)
		server.send(nome)

	elif data == "vitoria" or data == "derrota":
		print(data)
	else:
		jogo = data

	# print(data)

	# servidor ja mandou o jogo
	if jogo != None:
		# exibe os dados do jogo
		jogo.ExibirDados()
		# joga o turno
		jogo.TurnoJogar()

		# preparando para enviar
		data = pickle.dumps(jogo)
		# envia o jogo
		server.sendall(data)

		# exclui o jogo daqui?!
		
		jogo = None
		

	

server.close()



