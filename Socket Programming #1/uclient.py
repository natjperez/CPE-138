# Socket Programming 1: UDP Client
# CPE 138-04 Natalia Perez
# Due: March 6, 2022

from socket import *
serverName = '127.5.9.2'
serverPort = 17925
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input lowercase sentence: ')
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()
