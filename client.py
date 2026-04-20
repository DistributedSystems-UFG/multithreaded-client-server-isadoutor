import socket
import random
import time
from constCS import HOST, PORT

ops = ["add", "sub", "mul", "div"]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

start = time.time()

for _ in range(10000):
    op = random.choice(ops)
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    msg = f"{op} {a} {b}"
    s.send(msg.encode())

    data = s.recv(1024)
    print(msg, "=", data.decode())

end = time.time()

print("Tempo total:", end - start)

s.close()