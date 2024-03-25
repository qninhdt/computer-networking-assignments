import signal
import socket


def signal_handler(sig, frame):
    client_socket.close()
    server_socket.close()
    print("Server is stopped")
    exit(0)


signal.signal(signal.SIGINT, signal_handler)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))

server_socket.listen(1)
print("Server is listening")


while True:
    client_socket, client_address = server_socket.accept()
    print("Client is connected")

    while True:
        msg = client_socket.recv(1024).decode()

        if len(msg) == 0:
            client_socket.close()
            print("Client is disconnected")
            break

        print("[client]: {}".format(msg))

        response = msg.upper()
        client_socket.send(response.encode())
