import socket

HOST = '192.168.0.13'
PORT = 5555

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data: break
            print(f"Получено сообщение {data.decode()}")
            conn.sendall(data)
