"""Q8: Send a text file to the TCP receiver."""
from pathlib import Path
import socket
import struct

HOST, PORT = "127.0.0.1", 5008
path = Path(input("Text file path: "))
data = path.read_bytes()
with socket.create_connection((HOST, PORT)) as client:
    client.sendall(struct.pack("!Q", len(data)) + data)
    print("Server:", client.recv(1024).decode())
