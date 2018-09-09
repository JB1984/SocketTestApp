#Import the socket library
import socket
from threading import *

#Create a string array that holds all of our chat logs
chat = []

#Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket has been created")

#Specify a port that we want to reserve
port = 5000

#Bind this socket to the port. We can leave the first IP field as "" if we want to listen for all connections
#We could specify specific IP if we wanted to
s.bind(("",port))
print("Socket binded to {}".format(port))

#Put the socket into listening mode
s.listen(5)
print("Socket is listening")

#Create a forever loop until we interupt or error occurs
while True:

    #Establish a connection with the client
    c, addr = s.accept()
    print("Got connection from {}".format(addr))

    string = c.recv(1024).decode()
    print(string)
    chat.append(string)

    #Send a message back to client
    c.send("Thank you for connecting".encode())

    #Close the connection with client
    c.close()



