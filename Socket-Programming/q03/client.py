"""Q3: Ask the UDP server whether an integer is prime."""
import socket

HOST, PORT = "127.0.0.1", 5003
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.sendto(input("Integer: ").encode(), (HOST, PORT))
    print("Server:", client.recvfrom(1024)[0].decode())
