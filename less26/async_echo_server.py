# from select import select
# import socket
#
# HOST = 'localhost'
# PORT = 5555
# to_monitor = []
# SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SERVER_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# SERVER_SOCKET.bind((HOST, PORT))
# SERVER_SOCKET.listen()
#
#
# def accept(sock):
#     conn, adr = sock.accept()
#     to_monitor.append(conn)
#     print(f"{adr} has connected")
#
#
# def send_message(sock: socket.socket):
#     mess = sock.recv(1024)
#     if mess:
#         sock.sendall(mess)
#     else:
#         to_monitor.remove(sock)
#         sock.close()
#
#
# def event_loop():
#     while True:
#         ready_to_read, _, _ = select(to_monitor, [], [])
#         for sock in ready_to_read:
#             if sock == SERVER_SOCKET:
#                 accept(sock)
#             else:
#                 send_message(sock)
#
#
# if __name__ == '__main__':
#     to_monitor.append(SERVER_SOCKET)
#     event_loop()


import selectors
import socket

selector = selectors.DefaultSelector()


def init_server():
    HOST = 'localhost'
    PORT = 5555
    to_monitor = []
    SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    SERVER_SOCKET.bind((HOST, PORT))
    SERVER_SOCKET.listen()

    selector.register(fileobj=SERVER_SOCKET, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(sock):
    conn, adr = sock.accept()
    print(f"{adr} has connected")
    selector.register(fileobj=conn, events=selectors.EVENT_READ, data=send_message)


def send_message(sock: socket.socket):
    mess = sock.recv(1024)
    if mess:
        sock.sendall(mess)
    else:
        selector.unregister(sock)
        sock.close()


def event_loop():
    while True:
        events = selector.select()  # (key, events)
        # key ~ SelectorKey: NamedTuple
        # fileobj
        # events
        # data
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    init_server()
    event_loop()
