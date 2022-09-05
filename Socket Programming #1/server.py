# Socket Programming 2: TCP Client
# CPE 138-04 Natalia Perez
# Due: March 6 2022

from socket import *
serverName = '127.5.9.2'
serverPort = 17925
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input('Input lowercase sentence: ')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print 'From Server: ', modifiedSentence
clientSocket.close()
