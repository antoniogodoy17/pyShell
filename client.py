import socket

#Create the client socket object -> socket.socket()
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Get local machine name
host = socket.gethostname()

#Declare the port
port = 5000

#Connection to hostname on the declared port
c.connect((host,port))

#Declare bytes received, no more than 1024
tm = c.recv(1024)

#Close the connection
c.close()

print("Server Message: %s" %tm.decode('ascii'))