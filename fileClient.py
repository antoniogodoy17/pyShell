import socket
s = socket.socket()
def li():
	print "here are your files"

def search(filename,s):
	print ("searching: " + filename)
	s.send(filename)
	data = s.recv(1024)
	if data[:6] == 'EXISTS':
		filesize = long(data[6:])
		message = raw_input("File " + "'" + filename + "' " + "exists, size: " + str(filesize) + " bytes, do you want to download it? (Y/N)\n>>")
		if message == 'Y':
			s.send('OK')
			f = open('new_' + filename, 'wb')
			data = s.recv(1024)
			totalRecv = len(data)
			f.write(data)
			while totalRecv < filesize:
				data = s.recv(1024)
				totalRecv += len(data)
				f.write(data)
				print "{0:.2f}".format((totalRecv/float(filesize))*100)+"% Done"
			print "Download Complete"
	else:
		print "File does not exist"
def copy():
	pass

def update():
	pass

def upload():
	pass

def createFile():
	pass

def createFolder():
	pass

def move():
	pass

def Main():
	host = '127.0.0.1'
	port = 5000
	
	s.connect((host,port))
	
	instruction = raw_input(">>")
	while instruction != 'quit()':
		if instruction[:6] == 'search':
			fname = ""
			for i in range (7, len(instruction)):
				if i != len(instruction)-1:
					fname += instruction[i]
			search(fname,s)		
		if instruction == 'li()':
			li()
		instruction = raw_input(">>")
	print "Log out successful"
	s.close()

if __name__ == '__main__':
	Main()
