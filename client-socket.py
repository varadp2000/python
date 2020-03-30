import socket
s=socket.socket()

port=8080
conn=s.connect(('127.0.0.1',port))

while s.recv != '-' :
    print(s.recv(1024))
s.close()

