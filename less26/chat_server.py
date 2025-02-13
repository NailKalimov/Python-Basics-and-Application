import socket

HOST = 'localhost'
PORT = 5555

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                print(f"Получено сообщение {data.decode()}")
                if data.decode() == 'q':
                    conn.sendall(b'q')
                    break
                conn.sendall(input("Введите ответ: ").encode())
