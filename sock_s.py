from socket import *
from time import ctime

host = gethostname()
port = 1234
buffsize = 1024
addr = (host,port)

TcpServerSoc = socket(AF_INET,SOCK_STREAM)
TcpServerSoc.bind(addr)
TcpServerSoc.listen(10)
print 'tcp server name is %s, port is %s' %addr
while True:
    print 'waiting for connection..'
    c_sock,c_addr = TcpServerSoc.accept()
    print 'there is connection request from %s' %c_addr[0]
    print c_addr

    while True:
        data = c_sock.recv(buffsize)
        print data
        if not data:
            break;
        c_sock.send('[%s] %s' %(ctime(),data))
TcpServerSock.close()
