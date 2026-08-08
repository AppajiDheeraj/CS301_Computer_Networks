"""Q2: TCP arithmetic server."""
import json
import socket

HOST, PORT = "127.0.0.1", 5002

def calculate(left, operator, right):
    if operator == "+": return left + right
    if operator == "-": return left - right
    if operator == "*": return left * right
    if operator == "/": return left / right
    raise ValueError("operator must be +, -, *, or /")

with socket.socket() as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT)); server.listen()
    print(f"Q2 server listening on {HOST}:{PORT}")
    while True:
        conn, _ = server.accept()
        with conn:
            try:
                left, op, right = json.loads(conn.recv(1024).decode())
                answer = {"result": calculate(left, op, right)}
            except (ValueError, ZeroDivisionError, json.JSONDecodeError) as error:
                answer = {"error": str(error)}
            conn.sendall(json.dumps(answer).encode())
