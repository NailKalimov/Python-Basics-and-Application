import socket

HOST = '192.168.0.13'
PORT = 5555
ADDR = (HOST, PORT)

with socket.socket() as s:
    s.bind(ADDR)
    s.listen()
    print("Waiting connection...")
    conn, addr = s.accept()
    print(f'Connected with {addr}')
    with open('weather.json', 'rb') as f:
        while True:
            data = f.read(1024)
            if not data: break
            conn.send(data)
            print(f'Transmitted: {data}')
    print(f'Transmission completed')
