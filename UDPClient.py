import signal
import socket


def signal_handler(sig, frame):
    client_socket.close()
    print("Client is stopped")
    exit(0)


signal.signal(signal.SIGINT, signal_handler)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("[client]: ")
    client_socket.sendto(msg.encode(), ("localhost", 12345))

    data, server_address = client_socket.recvfrom(1024)
    print("[server]: {}".format(data.decode()))
