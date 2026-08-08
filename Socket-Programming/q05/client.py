"""Q5: Request counts for a file available to the server."""
import socket

HOST, PORT = "127.0.0.1", 5005
with socket.create_connection((HOST, PORT)) as client:
    client.sendall(input("Server-side filename: ").encode())
    print("Server:", client.recv(1024).decode())
