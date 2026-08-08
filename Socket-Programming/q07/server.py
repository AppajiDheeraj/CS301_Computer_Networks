"""Q7: TCP server that checks whether a string is a palindrome."""
import socket

HOST, PORT = "127.0.0.1", 5007
def is_palindrome(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

with socket.socket() as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT)); server.listen(); print(f"Q7 server listening on {HOST}:{PORT}")
    while True:
        conn, _ = server.accept()
        with conn:
            text = conn.recv(1024).decode()
            conn.sendall(f"{text!r} is {'a' if is_palindrome(text) else 'not a'} palindrome".encode())
