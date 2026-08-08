"""Q2: Send an arithmetic operation to the TCP server."""
import json
import socket

HOST, PORT = "127.0.0.1", 5002
left = float(input("First number: "))
operator = input("Operator (+, -, *, /): ")
right = float(input("Second number: "))
with socket.create_connection((HOST, PORT)) as client:
    client.sendall(json.dumps([left, operator, right]).encode())
    print(json.loads(client.recv(1024).decode()))
