import socket
s = socket.socket()
host = 'localhost'
port = 6001

s.connect((host, port))

filename = 'teste.xlsx'
with open(filename, 'wb') as f:
    print('Arquivo aberto')

    while True:
        print('Recebendo dados...')
        data = s.recv(1024*16)

        print('Dados recebidos:', data)
        
        if not data:
            break
        
        f.write(data)

    f.close()
    print('Transferência realizada com sucesso')
    s.close()
    print('Conexão fechada')