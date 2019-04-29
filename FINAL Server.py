import socket
import threading
from threading import Thread
from SocketServer import ThreadingMixIn
import time
from Crypto.Cipher import AES
import base64
import os


TCP_PORT = 60001
BUFFER_SIZE = 1024

def encrypt(privateInfo):

	BLOCK_SIZE = 16
	PADDING = '{'
	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
	EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
	secret = os.urandom(BLOCK_SIZE)
	print('encryption key:',secret)
	cipher = AES.new(secret)

	encoded = EncodeAES(cipher, privateInfo)
	return encoded


# try to detect whether IPv6 is supported at the present system and
# fetch the IPv6 address of localhost.
if not socket.has_ipv6:
  raise Exception("the local machine has no IPv6 support enabled")

addrs = socket.getaddrinfo("localhost", TCP_PORT, socket.AF_INET6, 0, socket.SOL_TCP)
# ALTERNATIVE:  socket.getaddrinfo("www.python.org", 80, 0, 0, socket.SOL_TCP)
# [(2, 1, 6, '', ('82.94.164.162', 80)),
#  (10, 1, 6, '', ('2001:888:2000:d::a2', 80, 0, 0))]


if len(addrs) == 0:
  raise Exception("there is no IPv6 address configured for localhost")

entry0 = addrs[0]
TCP_IP = entry0[-1]


print('TCP_IP=', print(TCP_IP))
print('TCP_PORT=',TCP_PORT)


class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print(" New thread started for "+ip+":"+str(port))

    def run(self):
        filename='mytext.txt'
        f = open(filename,'rb')
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(encrypt(l))
                print('Sent ',repr(l))
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.sock.close()
                break

tcpsock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# ALTERNATIVE:
# socket.getaddrinfo("www.python.org", 80, 0, 0, socket.SOL_TCP)
# [(2, 1, 6, '', ('82.94.164.162', 80)),
#  (10, 1, 6, '', ('2001:888:2000:d::a2', 80, 0, 0))]

# ourSocket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
# ourSocket.connect(('2001:888:2000:d::a2', 80, 0, 0))

tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print("server opened socket connection:", tcpsock, ", address: '%s'" % TCP_IP[0])
    print("Waiting for incoming connections...")

    (conn, (ip,port)) = tcpsock.accept()
    print('Got connection from ', (ip,port))
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    # When/How should I call the run function from the ClientThread class? 
    threads.append(newthread)

for t in threads:
    t.join()