#CLIENT, SERVER (COMMUNICATOR), VFS(LOGIC), LFS, SHELL, COORDINATOR, COMMENDPOINT, VOTES

#1.CLIENT -> SHELL
#2.SHELL -> SERVER
#3.SERVER -> COORDINATOR
#4.COORDINATOR -> LFS, VFS
#5 LFS -> COMMENDPOINT
#6 COMMENDPOINT -> VOTES
#7 COMMENPOINT -> COORDINATOR (WHEN ALL THE CLIENTS FINISHED VOTING)
#8 COORDINATOR -> VFS
#9 VFS -> VOTES
#10 VOTES -> COORDINATOR
#11 COORDINATOR -> VFS

#Client sends a message to the shell
#

#TODO:
	#Create tree structure interface (logical)
	#Create lfs interface
	#Create Shell
	#Create Server logic
	#Create Coordinator
	#Create 

import socket
import vfs as VFS
import lfs as LFS
import shell

#Create the client socket object -> socket.socket()
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Get local machine name
host = socket.gethostname()

#Declare the port
port = 5000

#Connection to hostname on the declared port
c.connect((host,port))

def main():
	vfs = None
	lfs = None

	s = shell.shell()
	s.run(c)

	# instruction = raw_input('>> ')
	# cmd = instruction.split()


	#c.close()

	# while instruction != 'quit':
	# 	if cmd[0] == 'init':
	# 		if(vfs!=None):
	# 			print("ERROR: Virtual File System already initialized")
	# 		else:
	# 			vfs = VFS.Tree()
	# 			print("VFS Initialized on " + vfs.home().path)

	# 	if cmd[0] == 'makedir':
	# 		name = cmd[1]
	# 		vfs.create(name,"d")

	# 	if cmd[0] == 'makefile':
	# 		name = cmd[1]
	# 		vfs.create(name,"f")

	# 	if cmd[0] == 'remove':
	# 		name = cmd[1]
	# 		if vfs.remove(name) == False:
	# 			print("ERROR: No such file " + name + "found in current directory.")
	# 		else:
	# 			print(name + " was removed succesfully.")

	# 	if cmd[0] == 'li':
	# 		vfs.li()
	# instruction = raw_input('>> ')
	# cmd = instruction.split()
	print "\nLog out successful\n"

	#Close the connection
	c.close()

if __name__ == '__main__':
	main()