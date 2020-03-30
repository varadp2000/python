import socket                   # Import socket module

port = 60000                # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()
print(host)
s.bind(('localhost', port))            # Bind to the port
s.listen(5)
print('Server listening....')

while True:
    conn, addr = s.accept()
# Establish connection with client.
    print ('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))
    filename='events.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()
    print('Done sending')
    print(conn.recv(1024))
    conn.send(b'Thank you for connecting')
    conn.close()
