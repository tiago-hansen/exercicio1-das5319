import socket
import time
import csv

s = socket.socket()
host = 'localhost'
port = 6001

s.connect((host, port))
print('Conexão estabelecida com o servidor')

filename = 'teste.csv'
with open(filename, 'ab') as f:
    print('Arquivo aberto')

    # Receive file size from server
    filesize = int(s.recv(1024).decode().strip().split()[0])
    print('Tamanho do arquivo:', filesize)

    # Receive file content from server
    received_size = 0
    while received_size < filesize:
        data = s.recv(1024*16)
        received_size += len(data)
        f.write(data)

    f.close()
    print('Arquivo recebido com sucesso')

# Append a new line to the received file
time.sleep(3)
with open(filename, 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Nova linha adicionada pelo cliente'])

s.close()
print('Conexão fechada')
