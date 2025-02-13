import socket

HOST = '192.168.0.13'
PORT = 5555

with socket.socket() as s:
    s.connect((HOST, PORT))
    s.sendall((input('Введите сообщение для отправки').encode()))
    print("Данные отправлены")
    data = s.recv(1024)
    print(f'Получено от сервера:  + {data.decode()}')
