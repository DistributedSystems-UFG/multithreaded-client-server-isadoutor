import socket
import threading
from constCS import HOST, PORT

def handle(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break

        op, a, b = data.decode().split()
        a = int(a)
        b = int(b)

        if op == "add":
            result = a + b
        elif op == "sub":
            result = a - b
        elif op == "mul":
            result = a * b
        elif op == "div":
            result = a / b
        else:
            result = "erro"

        conn.send(str(result).encode())

    conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    conn, addr = s.accept()
    t = threading.Thread(target=handle, args=(conn,))
    t.start()