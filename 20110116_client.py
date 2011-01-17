import socket

host = 'localhost'
port = 8000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.send(('2,5'))
adddata = s.recv(size)
s.close()
print ('Received:', adddata)
