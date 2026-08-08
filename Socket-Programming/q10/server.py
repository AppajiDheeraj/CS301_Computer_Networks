"""Q10: TCP server that sorts an array of integers."""
import json
import socket

HOST, PORT = "127.0.0.1", 5010
with socket.socket() as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT)); server.listen(); print(f"Q10 server listening on {HOST}:{PORT}")
    while True:
        conn, _ = server.accept()
        with conn:
            try:
                values = json.loads(conn.recv(4096).decode())
                if not all(isinstance(value, int) and not isinstance(value, bool) for value in values):
                    raise ValueError("send a JSON array of integers")
                reply = {"sorted": sorted(values)}
            except (ValueError, TypeError, json.JSONDecodeError) as error:
                reply = {"error": str(error)}
            conn.sendall(json.dumps(reply).encode())
