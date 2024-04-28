from socket import *

meu_host = '127.0.0.1'
minha_port = 50009

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((meu_host, minha_port))
sockobj.listen(1)

while True:
    conexao, endereco = sockobj.accept()
    print('Server conectado por', endereco)
    
    while True:
        data = conexao.recv(1024)
        print('Clinte enviou:', data.decode())
        resposta = 'Eco=>' + data.decode()
        conexao.send(resposta.encode())

conexao.close()