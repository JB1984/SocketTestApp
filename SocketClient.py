#Import the socket module
import socket

#Define port we want to use for connection
port = 5000

#Defind the server we want to connect to
server = '127.0.0.1'

def sendMessage(stringToSend):

    s = socket.socket()
    s.connect((server, port))

    s.send(stringToSend.encode())

    print(s.recv(1024))

    s.close()


while True:
    message = input("Please enter what you want to send here: ")
    sendMessage(message)



