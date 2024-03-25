import signal
import socket


def signal_handler(sig, frame):
    server_socket.close()
    print("Server is stopped")
    exit(0)


signal.signal(signal.SIGINT, signal_handler)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("localhost", 12345))

print("Server is listening")

while True:
    data, client_address = server_socket.recvfrom(1024)

    msg = data.decode()

    print("[client]: {}".format(msg))

    response = msg.upper()
    server_socket.sendto(response.encode(), client_address)
