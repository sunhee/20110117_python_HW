import socket

host = ''
port = 8000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while True:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        sdata = data.split(',')
        intsdata = [int(x) for x in sdata]
        #print (intsdata)
        adddata = sum(intsdata)
        #print (adddata)
        client.send(str(adddata))
    client.close()    
