# Socket Programming 1: UDP Server
# CPE 138-04 Natalia Perez
# Due: March 6, 2022

from socket import *
serverPort = 17925
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print 'The server is ready to receive'
while 1:
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.upper()
        serverSocket.sendto(modifiedMessage, clientAddress)
