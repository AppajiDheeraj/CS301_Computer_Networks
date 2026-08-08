"""Q6: UDP server that prints a message and the sender's address."""
import socket

HOST, PORT = "127.0.0.1", 5006
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT)); print(f"Q6 server listening on {HOST}:{PORT}")
    while True:
        data, (ip, port) = server.recvfrom(1024)
        print(f"Message from {ip}:{port}: {data.decode()}")
        server.sendto(b"Message received", (ip, port))
