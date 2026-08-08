"""Q5: TCP server that counts lines, words, and characters in a local file."""
from pathlib import Path
import socket

HOST, PORT = "127.0.0.1", 5005
BASE = Path.cwd().resolve()
with socket.socket() as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT)); server.listen(); print(f"Q5 server listening on {HOST}:{PORT}")
    while True:
        conn, _ = server.accept()
        with conn:
            try:
                path = (BASE / conn.recv(1024).decode()).resolve()
                if BASE not in path.parents or not path.is_file(): raise ValueError("file not found in server folder")
                text = path.read_text(encoding="utf-8")
                reply = f"lines={len(text.splitlines())}, words={len(text.split())}, characters={len(text)}"
            except (OSError, ValueError) as error:
                reply = f"Error: {error}"
            conn.sendall(reply.encode())
