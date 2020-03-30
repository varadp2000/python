import socket
s=socket.socket()
print("Socket Initialized")

port=8080
s.bind(('',port))
print("Socket Binded to port ",port)

s.listen(5)
print("Socket Listening")

while True:
    c,addr= s.accept()
    print("Got Connection from", addr)
    c.sendall(b'Send Data - to exit5')
    data = c.recv(1024)
    while data != b'-':
        data = c.recv(1024)
        print("Received",data)
    c.close()
