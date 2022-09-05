# Socket Programming 2: SMTP
# CPE 138-04 Natalia Perez
# Due: March 27, 2022

from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server and call it mailserver
# SMTP uses Port 25

mailserver = 'smtp.csus.edu'

# Create "clientSocket" and establish TCP connection
serverPort = 25
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, serverPort))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
        print('220 reply not received from server.')

# Send HELO command and print server response
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())

recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
        print('250 reply not received from server.')

# Send MAIL FROM command and print server response
mailCommand = 'MAIL FROM: <alice@csus.edu>\r\n'
clientSocket.send(mailCommand.encode())

recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
        print('250 reply not received from server.')

# Send RCPT TO command and print server response
rcptCommand = 'RCPT TO: <nataliaaa41401@gmail.com>\r\n'
clientSocket.send(rcptCommand.encode())

recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
        print('250 reply not received from server.')

# Send DATA command and print server response
dataCommand = 'DATA \r\n'
clientSocket.send(dataCommand.encode())

recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
        print('354 reply not received from server.')

# Send message data
clientSocket.send(msg)

# Message ends with a single period
clientSocket.send(endmsg)

recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
        print('250 reply not received from server.')

# Send QUIT command and get server response
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())

recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '221':
        print('221 reply not received from server.')

clientSocket.close()
