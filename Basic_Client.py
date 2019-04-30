import socket                   # Import socket module
import sys

s = socket.socket()             # Create a socket object

def main(serverAddr, serverPort):
    serverPort = int(serverPort)
    
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
    s.connect((serverAddr, serverPort, 0, 0))
    s.send("Hello server!")

    with open('received_file', 'wb') as f:
        print('file opened')
        while True:
            print('receiving data...')
            data = s.recv(1024)
            print('data=%s', (data))
            if not data:
                break
            # write data to a file
            f.write(data)

    f.close()
    print('Successfully get the file')
    s.close()
    print('connection closed')

if __name__ == "__main__":
    serverAddr = 'localhost'
    serverPort = 8080
    if len(sys.argv) > 1:
        serverAddr = sys.argv[1]
    if len(sys.argv) > 2:
        serverPort = sys.argv[2]
    main(serverAddr, serverPort)


