# Socket Programming 3: Web Server
# CPE 138-04 Natalia Perez
# Due: April 24th, 2022


#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 17925
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
        #Establish the connection
        print 'Ready to serve...'
        connectionSocket, addr = serverSocket.accept()

        try:
                message = connectionSocket.recv(1024)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()

                #Send one HTTP header line into socket
                httpHeader = "HTTP/1.1 200 OK\r\n\n\n"
                serverSocket.send(httpHeader)

                #Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                        connectionSocket.send(outputdata[i])
                connectionSocket.close()

        except IOError:
                #Send response message for file not found

                clientSocket.send('404 FILE NOT FOUND')

                #Close client socket
                clientSocket.close()

serverSocket.close()
