from socket import *

server_host = '127.0.0.1'
server_port = 50009

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((server_host, server_port))

while True:
    print('Digite uma mensagem')
    mensagem = input()
    sockobj.send(mensagem.encode())
    data = sockobj.recv(1024)
    print('Server recebeu:', data.decode())

sockobj.close()