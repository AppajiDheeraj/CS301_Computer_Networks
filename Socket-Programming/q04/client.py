"""Q4: Use the TCP echo server."""
import socket

HOST, PORT = "127.0.0.1", 5004
with socket.create_connection((HOST, PORT)) as client:
    while True:
        message = input("Message (exit to stop): ")
        client.sendall(message.encode())
        print("Server:", client.recv(1024).decode())
        if message.strip().lower() == "exit":
            break
