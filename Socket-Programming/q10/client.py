"""Q10: Send integers to the TCP sorting server."""
import json
import socket

HOST, PORT = "127.0.0.1", 5010
values = [int(value) for value in input("Integers separated by spaces: ").split()]
with socket.create_connection((HOST, PORT)) as client:
    client.sendall(json.dumps(values).encode())
    print("Server:", json.loads(client.recv(4096).decode()))
