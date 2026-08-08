"""Q7: Ask the TCP server to check a palindrome."""
import socket

HOST, PORT = "127.0.0.1", 5007
with socket.create_connection((HOST, PORT)) as client:
    client.sendall(input("Text: ").encode())
    print("Server:", client.recv(1024).decode())
