import signal
import socket


def signal_handler(sig, frame):
    client_socket.close()
    print("Client is stopped")
    exit(0)


signal.signal(signal.SIGINT, signal_handler)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

while True:
    msg = input("[client]: ")

    if len(msg) == 0:
        continue

    client_socket.send(msg.encode())

    response = client_socket.recv(1024).decode()
    print("[server]: {}".format(response))
