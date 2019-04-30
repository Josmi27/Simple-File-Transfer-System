import socket                   # Import socket module
import sys

s = socket.socket()             # Create a socket object

def main(serverAddr, serverPort):
    serverPort = int(serverPort)
    
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
    s.connect((serverAddr, serverPort, 0, 0))
    s.send(b"resource.txt")


    while True:
        print('receiving data...')
        data = s.recv(1024)
        contents = data.decode()

        if(contents == "File Not Found\n"):
            print("Client requested invalid filename")

        else:
            with open('received.txt', 'w') as writer:
                writer.write(contents)
                writer.close()
                f = open('received.txt', 'r')
                c = f.read()
                print(c)
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


