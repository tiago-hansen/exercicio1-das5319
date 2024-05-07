import socket
import time
import csv
import os

s = socket.socket()
host = 'localhost'
port = 8001

s.connect((host, port))
print('Conexão estabelecida com o servidor')

filename = 'client_data/FT_arquivo_recebido.xlsx'
with open(filename, 'wb') as f:
    print('Arquivo aberto')

    while True:
        print('Recebendo dados...')
        data = s.recv(1024*16)

        print('Dados recebidos:', data)
        
        if not data:
            break
        
        f.write(data)

    print('Arquivo recebido com sucesso')

print('Arquivo salvo em', filename)

time.sleep(3)

# Append a new line to the received xlsx file

# with open(filename, 'a') as f:
#     f.write('Novo dado\n')

# Send the modified file back to the server
with open(filename, 'rb') as f:
    l = f.read(1024*16)
    
    while (l):
        print('Enviando dados...')
        s.send(l)
        l = f.read(1024*16)

    print('Arquivo enviado de volta para o servidor')
    # f.close()

s.close()
print('Conexão fechada')
