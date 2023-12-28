from socket import socket, AF_INET, SOCK_STREAM

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5)
        while True:
            (clientsocket, address) = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if len(pieces) > 0:
                print(pieces[0])

            data = 'HTTP/1.1 200 OK\r\n'
            data += 'Content-Type: text/html; charset=utf-8\r\n'
            data += '\r\n'
            data += '<html><body>Hello World </body></html>\r\n\r\n'
            clientsocket.sendall(data.encode())
    except KeyboardInterrupt:
        print("\nShutting Down...\n")
    except Exception as exc:
        print("Error: \n")
        print(exc)

    serversocket.close()

print('Access http://localhost:9000')
createServer()
