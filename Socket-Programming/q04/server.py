"""Q4: TCP echo server; send 'exit' to close one client session."""
import socket

HOST, PORT = "127.0.0.1", 5004
with socket.socket() as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT)); server.listen(); print(f"Q4 server listening on {HOST}:{PORT}")
    while True:
        conn, address = server.accept()
        with conn:
            print("Connected:", address)
            while (message := conn.recv(1024)):
                if message.decode().strip().lower() == "exit":
                    conn.sendall(b"Goodbye"); break
                conn.sendall(message)
