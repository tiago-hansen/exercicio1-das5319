import socket
import os

port = 8001
s = socket.socket()
s.bind(('localhost', port))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Conectado por', addr)

    filename = 'server_data/FT_teste.xlsx'

    # Send file content to client
    with open(filename, 'rb') as f:
        l = f.read(1024*16)
        while (l):
            print('Enviando dados...')
            conn.send(l)
            l = f.read(1024*16)
        print('Arquivo enviado. Envio completo')
        # f.close()

    print('Arquivo enviado.')

    # Receive the file sent back by the client overriding the original file
    with open(filename, 'wb') as f:
        print('Arquivo aberto')

        while True:
            print('Recebendo dados...')
            data = conn.recv(1024*16)

            print('Dados recebidos:', data.decode())
            
            if not data:
                break
            
            f.write(data)
        
        # f.close()

        print('Arquivo recebido de volta do cliente')

    print('Arquivo salvo em', filename)
    conn.close()
    print('Conexão fechada')
