#Import the socket module
import socket

#Create a socket object
s = socket.socket()

#Define port we want to use for connection
port = 5000

#Connect to the server on local computer
s.connect(('127.0.0.1', port))

#Recieve data from the server
print(s.recv(1024))

#Close the connection
s.close()