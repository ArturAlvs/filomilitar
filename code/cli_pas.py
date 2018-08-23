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

data = "espectador".encode()
server.send(data)

jogo = None


while True:
	data = server.recv(4096)
	if not data:
		break
	# data = data.decode()
	data = pickle.loads(data)
	
	if data == "Jogador com mais pontos ganhou o jogo.":
		print(data)
	else:
		jogo = data

	# servidor ja mandou o jogo
	if jogo != None:
		# exibe os dados do jogo
		jogo.ExibirDados()

		# exclui o jogo daqui?!
		
		jogo = None
		

server.close()
