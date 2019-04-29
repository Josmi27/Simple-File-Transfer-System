# client3.py on local machine
#!/usr/bin/env python

#!/usr/bin/env python

import socket
import time
from Crypto.Cipher import AES
import base64
import os

TCP_IP = 'localhost'
TCP_PORT = 60001
BUFFER_SIZE = 1024


def decrypt(encryptedString):
	PADDING = '{'
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
	#Key is FROM the printout of 'secret' in encryption
	#below is the encryption.
	encryption = encryptedString
	key = ''
	cipher = AES.new(key)
	decoded = DecodeAES(cipher, encryption)
	return decoded


s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

clock_start = time.clock()
time_start = time.time()

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(BUFFER_SIZE)
        print('encrypted data=%s', (data))
        data = decrypt(s.recv(BUFFER_SIZE))
        print('decrypted data=%s', (data))
        if not data:
            f.close()
            print('file close()')
            break
        # write data to a file
        f.write(data)

print('Successfully get the file')
s.close()
print('connection closed')

clock_end = time.clock()
time_end = time.time()

duration_clock = clock_end - clock_start
print('clock:  start = ',clock_start, ' end = ',clock_end)
print('clock:  duration_clock = ', duration_clock)

duration_time = time_end - time_start
print('time:  start = ',time_start, ' end = ',time_end)
print('time:  duration_time = ', duration_time)