#Estructura
#{'type':user/system/control, 'cmd': , 'category':none/vote/confirmation, 'args': }
class Message:
	def __init__(self):
		#self.contrl{type: }
		#self.payLoad{
		#
		#}
		self.type = "None"
		self.cmd = "None"
		self.options = "None"
		self.file = "None"
		self.path = "None"
		self.category = "None"

	def setType(self,entry):
		self.type = entry

	def setCmd(self,entry):
		self.cmd = entry

	def setOptions(self,entry):
		self.option = entry

	def setFile(self,entry):
		self.file = entry

	def setPath(self,entry):
		self.path = entry

	def setCategory(self,entry):
		self.category = entry

	def type(self):
		return self.type

	def cmd(self):
		return self.cmd

	def option(self):
		return self.option

	def file(self):
		return self.file

	def path(self):
		return self.path

	def category(self):
		return self.category

	def marshal(self,json):
		#Recibe una cadena y la transforma a un objeto Message
		values = []
		json = json[1:-1]
		jsonList = json.split(',')
		message = Message()

		for item in jsonList:
			value = item.split(':')[1]
			values.append(value)

		message.setType(values[0])
		message.setCmd(values[1])
		message.setOptions(values[2])
		message.setFile(values[3])
		message.setPath(values[4])	
		message.setCategory(values[5])

		return message

	def demarshal(self,message):
		#Recibe un objeto Message y lo transforma a una cadena tipo json
		json = "{"+"'type':" + str(message.type) +"," +"'cmd':" + str(message.cmd) + "," + "'options':" + str(message.options) + "," +"'file':" + str(message.file) + "," +"'path':" + str(message.path) + "," + "'category':" + str(message.category) + "}"
		return json

	def parse(self,string):
		cmd = string.split()[0]

		if cmd == 'cls':
			instruction = string.split()
			cmdType = "user"
			json = "{'type':" + cmdType +",'cmd':" + cmd + ",'options':None,'file':None,'path':None,'category':None}"
			return json

		if cmd == 'help':
			instruction = string.split()
			cmdType = "user"
			json = "{'type':" + cmdType +",'cmd':" + cmd + ",'options':None,'file':None,'path':None,'category':None}"
			return json

		if cmd in ('makedir','rmdir','makefile'):
			instruction = string.split()
			args = "None"
			if len(instruction)>1:
				args = string.split()[1:]

			cmdType = "system"
			fileName = args[0]
			path = "None"
			if len(args) > 1:
				path = args[0]

			json = "{'type':" + cmdType +",'cmd':" + cmd + ",'options':None,'file':" + fileName + ",'path':" + path + ",'category':None}"
			return json

		if cmd == 'li':
			instruction = string.split()
			cmdType = "system"
			
			json = "{'type':" + cmdType +",'cmd':" + cmd + ",'options':None,'file':None,'path':None,'category':None}"
			return json

		if cmd == 'cd':
			instruction = string.split()
			args = "None"
			if len(instruction)>1:
				args = string.split()[1:]

			cmdType = "system"
			path = args[0]

			json = "{'type':" + cmdType +",'cmd':" + cmd + ",'options':None,'file':None,'path':" + path + ",'category':None}"
			return json

		if cmd == 'cwd':
			instruction = string.split()
			cmdType = "system"
			
			json = "{'type':" + cmdType +",'cmd':" + cmd + ",'options':None,'file':None,'path':None,'category':None}"
			return json
