"""Q9: Send a sentence for TCP string analysis."""
import socket

HOST, PORT = "127.0.0.1", 5009
with socket.create_connection((HOST, PORT)) as client:
    client.sendall(input("Sentence: ").encode())
    print("Server:", client.recv(1024).decode())
