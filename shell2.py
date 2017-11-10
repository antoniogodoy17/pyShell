import socket
import os
import vfs as VFS 
import lfs 

cmdDic = {'init': 'Initialize the Virtual File System','cd':'Enters to a specified directory','makedir':'Creates a new directory','makefile':'Creates a new file','remove':'Removes a file or an entire directory','li':'List all items of the current directory','cls':'Clean command line','quit':'Exit from shell','help':'List commands, description and syntax'}

class shell:
	def __init__(self):
		self.socket = None
		self.vfs = None
		self.cls = "user@:~" + os.getcwd() + "/$ "
		self.currentUser = None

	def run(self,c):
		self.socket = c
		self.prompt()

	def findCommand(self,cmd, args):
		if cmd not in cmdDic.keys():
			print("ERROR: Command not found. \nIf assistance is needed, type the 'help' command.")
		else:
			if cmd == 'cls':
				lfs.clear()

			if cmd == 'help':
				lfs.help()

			if cmd == 'makedir':
				if args != None:
					name = args[0]
					self.vfs.create(name,"d")
				else:
					print("Invalid arguments were given.")

			if cmd == 'makefile':
				if args != None:
					name = args[0]
					self.vfs.create(name,"f")
				else:
					print("Invalid arguments were given.")

			if cmd == 'remove':
				if args != None:
					name = args[0]
					if self.vfs.remove(name) == False:
						print("ERROR: No such file " + name + "found in current directory.")
					else:
						print(name + " was removed succesfully.")
				else:
					print("Invalid arguments were given.")

			if cmd == 'li':
				lfs.li()
			if cmd == 'cd':
				if args != None:
					lfs.cd(args[0])
					# directory = args[0]
					# self.vfs.cd(directory)
					# self.cls = "shell/"
					# for directory in self.vfs.currentDir:
					# 	self.cls += directory
					# self.cls += "$:"

	def prompt(self):
		cmd = ''
		while cmd != 'quit':
			self.cls = "user@:~" + os.getcwd() + "/$ " 
			instruction = raw_input(self.cls)
			cmd = instruction.split()[0]
			if len(instruction.split()) > 1:
				args = instruction.split()[1:]
			else:
				args = None
			self.findCommand(cmd,args)
		print("\nLog out from shell successfull.")