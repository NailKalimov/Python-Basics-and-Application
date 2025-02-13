import socket

HOST, PORT = 'localhost', 5555
data = b''
with socket.socket() as s:
    s.connect((HOST, PORT))
    while True:
        if data.decode() == 'q':
            break
        s.sendall(input("Введите текст сообщения: ").encode())
        data = s.recv(1024)
        print(f'получено сообщение: {data.decode()}')
