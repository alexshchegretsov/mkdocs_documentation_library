`simple http server`
=


```
import socket

def server():
    # AF_INET and SOCK_STREAM create tcp/ip socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind socket to localhost:9004
    server_socket.bind(("localhost", 9004))
    # listen incoming signals on port 9004 
    server_socket.listen()
    while True:
        # recieve incoming signal from 9004 port
        client_connection, client_address = server_socket.accept()
	# recieve raw request string with headers
        request = client_connection.recv(1024)
        request = request.decode().split("\r")
        # clean headers
        for header in request:
            print(header.strip())
        # send message in current connection
        client_connection.sendall(b"HTTP/1.1 200 OK\n\nHello!")
        # close connection and wait for a new request
        client_connection.close()

```
