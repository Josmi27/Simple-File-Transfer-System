'''
A simple example of an IPv6 server/client written in Python.
'''
import threading
import socket
import time

def fetch_local_ipv6_address(port=50000):
  # try to detect whether IPv6 is supported at the present system and
  # fetch the IPv6 address of localhost.
  if not socket.has_ipv6:
    raise Exception("the local machine has no IPv6 support enabled")

  addrs = socket.getaddrinfo("localhost", port, socket.AF_INET6, 0, socket.SOL_TCP)
  # example output: [(23, 0, 6, '', ('::1', 10008, 0, 0))]

  if len(addrs) == 0:
    raise Exception("there is no IPv6 address configured for localhost")

  entry0 = addrs[0]
  sockaddr = entry0[-1]
  return sockaddr

def ipv6_echo_server():
  # Echo server program

  s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
  sockaddr = fetch_local_ipv6_address()
  s.bind(sockaddr)
  s.listen(1)
  print ("server opened socket connection:", s, ", address: '%s'" % sockaddr[0])
  conn, addr = s.accept()

  time.sleep(1)
  print ('Server: Connected by', addr)
  if True: # answer a single request
    data = conn.recv(1024)
    conn.send(data)
    conn.close()

ipv6_echo_server()
