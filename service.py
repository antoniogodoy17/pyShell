from abc import ABCMeta, abstractmethod
from message import Message
import os
import shutil
import stat
from ktree import Ktree

cmdDic = {'cd':'Enters to a specified directory','makedir':'Creates a new directory','makefile':'Creates a new file','remove':'Removes a file or an entire directory','li':'List all items of the current directory','cls':'Clean command line','quit':'Exit from shell','help':'List commands, description and syntax'}

class Service(object):
    __metaclass__ = ABCMeta
     
    @abstractmethod
    def execute(self):
        pass

class ULC(Service):
	def execute(self,msg):
		pass
		#LLamadas a sistema relacionadas con la tarjeta de video se 
		#ejecutan en la consola del coordinador
		#Etiquetar al mensaje para saber de donde proviene y
		#que pueda enviar el mensaje al shell

		if msg.cmd == 'cls':
			print("soy un cls")
		# 	#os.system('clear')

		if msg.cmd == 'help':
			print("\n\tCommand : Description")
			for command in cmdDic.keys(): 
				print("\t"+ command + " : " + str(cmdDic[command]))
			print("\n")

		if msg.cmd == 'li':
			items = os.listdir(".")
			print("\nFiles:")
			for item in items:
				print("\t"+item)
			print("\n")
	
		if msg.cmd == 'cwd':
			print(os.getcwd())

class SLC(Service):
	def execute(self,msg):	
		if msg.file != "None":
			if msg.path != "None":
				pass
			else:
				pState = None
				if msg.cmd == 'makedir':
					pState = os.mkdir(msg.file,0o777)
				elif msg.cmd == 'rmdir':
					pState = shutil.rmtree(msg.file, ignore_errors=False, onerror=None)
				elif msg.cmd == 'makefile':
					pState = os.mknod(msg.file,0o600,stat.S_IRUSR)
				elif msg.cmd == 'rmfile':
					pState = os.remove(msg.file)
				elif msg.cmd == 'cd':
					if arg == '..':
						path = os.getcwd().rsplit("/",1)[0]
						os.chdir(path)
						#Evitar que home suba y crashee
					else:
						os.chdir(os.getcwd() + "/" + msg.file)
						#Evitar que crhasee hacia adelante cuando no existe carpeta o archivo
			if pState == None:
				print("Process returned: ",pState)
			else:
				print("Process Error: ",pState)
		else:
			print('Invalid arguments were given')


class CLC(Service):
	def execute(self,msg):
		print("Executing CLC / " + msg.cmd)
