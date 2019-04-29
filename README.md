# Simple-File-Transfer-System
The device used for this project is raspberry pi running linux os with each device as part of a mesh network running on ​openthread​. Each device runs a multithreaded server and a client program which allows for file request and response. Since openthread only permits the use of ipv6, all of the socket communication between devices use ipv6 instead of ipv4.

Some of the key features in the application include:
* Returning a file requested by the client (after a user specifies the file path being requested from the server)
* Displaying an appropriate error message if the file is not found
* Displaying the round trip time of each file request</p>

