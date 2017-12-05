import os
import socket
from message import Message

#Commands Directory
#Add the command type to the command so it can be sent as an argument to the coomunicator
cmdDic = ['cd','makedir','makefile','remove','li','cls','quit','help','rmfile','rmdir']

#Set up the COmmand Line Bash (clb)
clb = "user@:~" + os.getcwd() + "/$ "

#Create the client socket object -> socket.socket()
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Get local machine name
host = '127.0.0.1'#socket.gethostname()

#Declare the port
port = 9000

#Connection to hostname on the declared port
c.connect((host,port))

def prompt():
	cmd = ''
	while True:
		clb = "user@:~" + os.getcwd() + "/$ " 
		instruction = raw_input(clb)
		cmd = instruction.split()[0]

		if cmd not in cmdDic:
			print("ERROR: Command not found. \nIf assistance is needed, type the 'help' command.")
		elif cmd == 'quit':
			print("(Logged out from shell)")
			break
		else:
			message = Message()
			message = message.parse(instruction)
			c.sendall(message)
	c.close()

if __name__ == '__main__':
	prompt()