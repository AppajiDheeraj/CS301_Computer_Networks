"""Q9: TCP server that counts vowels, consonants, and words."""
import socket

HOST, PORT = "127.0.0.1", 5009
def analyse(text):
    letters = [char.lower() for char in text if char.isalpha()]
    return {"vowels": sum(char in "aeiou" for char in letters),
            "consonants": sum(char not in "aeiou" for char in letters),
            "words": len(text.split())}

with socket.socket() as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT)); server.listen(); print(f"Q9 server listening on {HOST}:{PORT}")
    while True:
        conn, _ = server.accept()
        with conn:
            result = analyse(conn.recv(1024).decode())
            conn.sendall(", ".join(f"{name}={value}" for name, value in result.items()).encode())
