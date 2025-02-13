import socket

HOST = '192.168.0.13'
PORT = 5555
ADDR = (HOST, PORT)

with socket.socket() as s:
    s.connect(ADDR)
    with open('input_data.json', "wb") as f:
        while True:
            data = s.recv(1024)
            if not data: break
            f.write(data)
        print("Receiving completed")
