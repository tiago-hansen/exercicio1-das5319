from socket import *

meu_host = '127.0.0.1'
minha_port = 50009

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((meu_host, minha_port))
sockobj.listen(1)

print("Aguardando conexão...")

conexao, endereco = sockobj.accept()
print('Server conectado por', endereco)

while True:
    data = conexao.recv(1024)
    if not data: 
        break
    print('Clinte:', data.decode())
    print('Você (Server): ')
    mensagem = input()
    conexao.send(mensagem.encode())

conexao.close()