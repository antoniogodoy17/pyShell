import socket
import os
import vfs as VFS 
import lfs as LFS

cmdDic = {'init': 'Initialize the Virtual File System','cd':'Enters to a specified directory','makedir':'Creates a new directory','makefile':'Creates a new file','remove':'Removes a file or an entire directory','li':'List all items of the current directory','cls':'Clean command line','quit':'Exit from shell','help':'List commands, description and syntax'}

class shell:
	def __init__(self,state="death"):
		self.state = state
		self.socket = None
		self.vfs = None
		self.lfs = None
		self.cls = "shell/home/$: "

	def run(self,c):
		self.state = "alive"
		self.socket = c
		self.prompt()

	def findCommand(self,cmd, args):
		if cmd not in cmdDic.keys():
			print("ERROR: Command not found")
		else:
			if cmd == 'init':
				if(self.vfs!=None):
					print("ERROR: Virtual File System already initialized")
				else:
					self.vfs = VFS.Tree()
					print("VFS Initialized on " + self.vfs.home().path)

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
				self.vfs.li()

			if cmd == 'cd':
				if args != None:
					directory = args[0]
					self.vfs.cd(directory)
					self.cls = "shell/"
					for directory in self.vfs.currentDir:
						self.cls += directory
					self.cls += "$:"

			if cmd == 'cls':
				os.system('clear')

			if cmd == 'help':
				for command in cmdDic.keys(): 
					print("\t"+ command + "\t" + str(cmdDic[command]))

			if cmd == 'quit':
				self.state = "death"
				print("\nLog out from shell successfull.")

	def prompt(self):
		while self.state == "alive":
			instruction = raw_input(self.cls)
			cmd = instruction.split()[0]
			if len(instruction.split()) > 1:
				args = instruction.split()[1:]
			else:
				args = None

			self.findCommand(cmd,args)