import socket
import os

port = 6001
s = socket.socket()
s.bind(('localhost', port))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Conectado por', addr)

    filename = 'teste.csv'
    filesize = os.path.getsize(filename)

    # Send file size to client
    conn.send(str(filesize).encode())

    # Send file content to client
    with open(filename, 'rb') as f:
        while True:
            data = f.read(1024*16)
            if not data:
                break
            conn.send(data)

    print('Arquivo enviado.')

    # Receive the file sent back by the client
    with open(filename, 'wb') as f:
        # Receive file size from client
        filesize = int(conn.recv(1024).decode())

        # Receive file content from client
        received_size = 0
        while received_size < filesize:
            data = conn.recv(1024*16)
            received_size += len(data)
            f.write(data)

        print('Arquivo recebido de volta do cliente')

    conn.close()
    print('Conexão fechada')
