from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
(conn, addr) = s.accept()
while True:
    data = conn.recv(1024)
    if not data: break
    op, a, b = bytes.decode(data).split()
    a, b = float(a), float(b)
    if op == "add":        result = a + b
    elif op == "sub": result = a - b
    elif op == "mult": result = a * b
    elif op == "div":   result = a / b
    elif op == "pow":    result = a ** b
    conn.send(str.encode(str(result)))
conn.close()
