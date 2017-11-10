import os

termid = os.ctermid() #Return the filename corresponding to the controlling terminal of the process
home = os.environ['HOME']
cwd = os.getcwd()
#os.listdir(path=".") return a list containing the names of the entries in the directory given.
#os.chdir(path): change the current working directory to path
#os.mkdir(path,mode=0o777,*,dir_fd=None)
#os.remove(path,*,dir_fd=None) remove the file path (file)
#os.rmdir(path,*,dir_fd=None)
#os.rename(src,dst,*,src_dir_fd=None,dst_dir_fd=None)
#os.walk(top,topdown=True,onerror=None,followlinks=False) returns 3-tuple(dirpath, dirnames, filenames), dirpath is a string path to directory

cmdDic = {'init': 'Initialize the Virtual File System','cd':'Enters to a specified directory','makedir':'Creates a new directory','makefile':'Creates a new file','remove':'Removes a file or an entire directory','li':'List all items of the current directory','cls':'Clean command line','quit':'Exit from shell','help':'List commands, description and syntax'}


def getcwd():
	print(os.getcwd())

def clear():
	os.system('clear')

def help():
	print("\n\tCommand : Description")
	for command in cmdDic.keys(): 
		print("\t"+ command + " : " + str(cmdDic[command]))
	print("\n")

def cd(arg):
	if arg == '..':
		path = os.getcwd().rsplit("/",1)[0]
		os.chdir(path)
		#Evitar que home suba y crashee
	else:
		os.chdir(os.getcwd() + "/" + arg)
		#Evitar que crhasee hacia adelante cuando no existe carpeta o archivo
def li():
	for  root, dirs, files in os.walk(str(os.getcwd()), topdown=False):
	   for name in files:
	      print(os.path.join(root, name))
	   for name in dirs:
	      print(os.path.join(root, name))
# class Tree:
# 	current = None

# 	def __init__(self, name="root", nodeType="d"):
# 		self.name = name
# 		self.nodeType = nodeType 
# 		self.root = None
# 		self.files = []
# 		self.path = "home/"#os.getenv("HOME") 
# 		self.ext = None
# 		self.current = self
# 		self.currentDir = [self.path]

# 	def home(self):
# 		if self.root == None:
# 			return self
# 		return self.root.home()

# 	def create(self, name, path):
# 		# for x in self.current.files:
# 		# 	if name+"/"  self.current.files:
		
# 		new = Tree(name, nodeType)
# 		self.current.files.append(new)
# 		new.root = self.current

# 	def rm(self,name):
# 		for fileSearched in self.files:
# 			if fileSearched.name == name:
# 				fileSearched.root.files.remove(self)
# 				fileSearched.root = None
# 			return True
# 		return False

# 	def li(self):
# 		for fileFound in self.current.files:
# 			print(fileFound.nodeType + "\t" + fileFound.name)

# 	def cd(self,name):
# 		if name == "..":
# 			if self.current.name != "root":
# 				self.currentDir.pop(-1)
# 				self.current = self.current.root
# 				print("Now current is: ",self.current.name)
# 		else:
# 			for node in self.current.files:
# 				if node.name == name:
# 					if node.nodeType == 'd':
# 						self.currentDir.append(node.name+"/")
# 						self.current = node
# 					else:
# 						print("Please enter a valid directory.")

