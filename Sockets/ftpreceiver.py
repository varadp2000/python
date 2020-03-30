import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect(('localhost', port))
s.send(b'Hello server!')

with open('Received1.txt', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print((data))
        f.write(data)
        if not data:
#            s.send(b'Data Received...Thank You')
            break
f.close()
print('Successfully got the file')
s.close()
print('connection closed')