import socket
import time

#Create the server socket object -> socket.socket()
#AF_INET address family
#SOCK_STREAM socket type (STREAM is quick and usefull)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Get local machine name
host = socket.gethostname()

#Declare the port
port = 5000

#Bind socket to the port -> socket.bind(address)
s.bind((host,port))

#Specify how many requests will listen at the same time (queue) -> socket.listen(backlog), min=0, max=5 (system dependent)
s.listen(5)

while True:
	#Establish connection -> socket.accept() retunrs a pair value (conn,address) where conn is a new socket object (to send and recieve data on the connection) and address is the adress bound to the socket on the other end of the connection.
	#.accept() creates a new socket used to communicate with it. In TCP servers, this is not the case, the socket created here is only used to returns a new socket.
	(clientSocket,addr) = s.accept()

	print("Connection with %s: successful." %str(addr))

	#Get system current time
	cTime = time.ctime(time.time()) + "\r\n"

	#Send to the client cTime variable -> socket.send(bytes[,flags]), send data to the socket, which should be connected to a remote socket. Returns the number of bytes sent.
	#Python 3, all strings are unicode, so it has to be encoded and decoded when sended and received.
	clientSocket.send(cTime.encode('ascii'))

	#Close the connection -> socket.close(), mark the socket closed, all future operations on the socket object will fail.
	clientSocket.close()
