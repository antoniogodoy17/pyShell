import os

class Ktree:
	current = None

	def __init__(self, name="root", nodeType="d"):
		self.name = name
		self.nodeType = nodeType
		self.root = None
		self.files = []
		self.path = "home/"#os.getenv("HOME") 
		self.ext = None
		self.current = self
		self.currentDir = [self.path]
		self.sysDir = os.getenv("HOME")		
		self.relTable = {self.path:self.sysDir}
		self.names = {"d":[],"f":[]}
		self.users = {"root":"1234"}
		print(self.relTable)

	def home(self):
		if self.root == None:
			return self
		return self.root.home()

	def create(self, name, nodeType, files = None):
		if name in self.names[nodeType]:
			print("There is a file with that name.")
		else:
			self.names[nodeType].append(name)
			new = Ktree(name, nodeType)
			self.current.files.append(new)
			new.root = self.current

	def rm(self,name):
		for fileSearched in self.files:
			if fileSearched.name == name:
				fileSearched.root.files.remove(self)
				fileSearched.root = None
			return True
		return False

	def li(self):
		for fileFound in self.current.files:
			print(fileFound.nodeType + "\t" + fileFound.name)

	def cd(self,name):
		if name == "..":
			if self.current.name != "root":
				self.currentDir.pop(-1)
				self.current = self.current.root
				print("Now current is: ",self.current.name)
		else:
			for node in self.current.files:
				if node.name == name:
					if node.nodeType == 'd':
						self.currentDir.append(node.name+"/")
						self.current = node
					else:
						print("Please enter a valid directory.")
	# def login(self, user, password):
	# 	for u in self.users.keys():
	# 		if u == user:
	# 			if password == self.users[user]:
	# 				return True
	# 			print("Incorrect password.")
	# 			return False
	# 	print("User not found.")
	# 	return False

