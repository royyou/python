from socket import *

host = 'ubuntu'
port = 1234
buffsize = 1024
addr = (host,port)
print 'connect to %s..' %host
c_sock = socket(AF_INET,SOCK_STREAM)
c_sock.connect(addr)

while True:
    data = raw_input('>  ')
    if not data:
        break;
    c_sock.send(data)
    data = c_sock.recv(buffsize)
    if not data:
        break;
    print data
c_sock.close()
