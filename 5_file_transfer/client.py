import socket
import time

s = socket.socket()
host = 'localhost'
port = 6001

s.connect((host, port))
print('Conexão estabelecida com o servidor')

filename = 'teste.csv'
with open(filename, 'ab') as f:
    print('Arquivo aberto')

    # Receive file size from server
    filesize = int(s.recv(1024).decode())

    # Receive file content from server
    received_size = 0
    while received_size < filesize:
        data = s.recv(1024*16)
        received_size += len(data)
        f.write(data)

    print('Arquivo recebido com sucesso')

# Append a new line to the received file
time.sleep(3)
with open(filename, 'ab') as f:
    f.write(b'\nNova linha adicionada pelo cliente')

# Send the modified file back to the server
with open(filename, 'rb') as f:
    # Send file size to server
    s.send(str(filesize).encode())

    # Send file content to server
    while True:
        data = f.read(1024*16)
        if not data:
            break
        s.send(data)

    print('Arquivo modificado enviado de volta para o servidor')

s.close()
print('Conexão fechada')
