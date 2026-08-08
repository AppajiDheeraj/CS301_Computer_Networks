"""Q6: Send a UDP text message."""
import socket

HOST, PORT = "127.0.0.1", 5006
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.sendto(input("Message: ").encode(), (HOST, PORT))
    print("Server:", client.recvfrom(1024)[0].decode())
