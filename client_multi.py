import socket
import threading
import random
import time
from constCS import HOST, PORT

ops = ["add", "sub", "mul", "div"]

def send_request():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    op = random.choice(ops)
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    msg = f"{op} {a} {b}"
    s.send(msg.encode())

    data = s.recv(1024)
    print(msg, "=", data.decode())

    s.close()

threads = []

start = time.time()

for _ in range(10000):
    t = threading.Thread(target=send_request)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print("Tempo total:", end - start)