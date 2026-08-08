"""Q8: TCP file receiver. The first 8 bytes contain the file length."""
from pathlib import Path
import socket
import struct

HOST, PORT = "127.0.0.1", 5008
OUTPUT = Path("received_file.bin")
def receive_exactly(conn, size):
    data = b""
    while len(data) < size:
        chunk = conn.recv(size - len(data))
        if not chunk: raise ConnectionError("connection closed before file completed")
        data += chunk
    return data

with socket.socket() as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT)); server.listen(); print(f"Q8 server listening on {HOST}:{PORT}")
    while True:
        conn, _ = server.accept()
        with conn:
            size = struct.unpack("!Q", receive_exactly(conn, 8))[0]
            OUTPUT.write_bytes(receive_exactly(conn, size))
            print(f"Saved {size} bytes to {OUTPUT}")
            conn.sendall(b"File received")
