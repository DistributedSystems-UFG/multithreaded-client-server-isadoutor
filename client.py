from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    request = input("> ")
    if request == "quit": break
    s.send(str.encode(request))
    data = s.recv(1024)
    print(bytes.decode(data))
s.close()
