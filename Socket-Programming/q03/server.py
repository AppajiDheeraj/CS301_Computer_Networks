"""Q3: UDP server that tests whether an integer is prime."""
import socket

HOST, PORT = "127.0.0.1", 5003
def is_prime(number):
    return number > 1 and all(number % divisor for divisor in range(2, int(number ** 0.5) + 1))

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT)); print(f"Q3 server listening on {HOST}:{PORT}")
    while True:
        data, address = server.recvfrom(1024)
        number = int(data.decode())
        server.sendto(f"{number} is {'prime' if is_prime(number) else 'not prime'}".encode(), address)
