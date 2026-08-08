"""Q1: TCP server that converts received text to uppercase."""
import socket

HOST, PORT = "127.0.0.1", 5001

with socket.socket() as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Q1 server listening on {HOST}:{PORT}")
    while True:
        conn, address = server.accept()
        with conn:
            message = conn.recv(1024).decode()
            print(f"{address}: {message}")
            conn.sendall(message.upper().encode())
