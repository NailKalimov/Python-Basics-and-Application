import json
import socket
from threading import Thread

NUMBERS_OF_USERS = 5
HOST = 'localhost'
PORT = 5555
ADDR = (HOST, PORT)
addresses = dict()


def chat_with_user(client_socket: socket.socket, client_addr):
    with client_socket:
        print(f'User {client_addr} connected!')
        while True:
            mess = client_socket.recv(1024).decode()
            if mess == '': break
            print(f'Received message from {client_addr}: {mess}')
            with open("weather.json", 'r') as f:
                data = json.load(f)
                client_socket.sendall(json.dumps(data[mess]).encode())


with socket.socket() as SERVER_SOCK:
    SERVER_SOCK.bind(ADDR)
    SERVER_SOCK.listen(NUMBERS_OF_USERS)

    while True:
        conn, addr = SERVER_SOCK.accept()
        addresses[conn] = addr
        Thread(target=chat_with_user, args=(conn, addr)).start()
