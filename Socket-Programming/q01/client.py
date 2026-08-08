"""Q1: Send text to the uppercase TCP server."""
import socket

HOST, PORT = "127.0.0.1", 5001
message = input("Text: ")
with socket.create_connection((HOST, PORT)) as client:
    client.sendall(message.encode())
    print("Server:", client.recv(1024).decode())
