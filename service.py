from abc import ABCMeta, abstractmethod
from message import Message
import os
import shutil
import stat

cmdDic = {'cd':'Enters to a specified directory','makedir':'Creates a new directory','makefile':'Creates a new file','remove':'Removes a file or an entire directory','li':'List all items of the current directory','cls':'Clean command line','quit':'Exit from shell','help':'List commands, description and syntax'}

class Service(object):
    __metaclass__ = ABCMeta
     
    @abstractmethod
    def execute(self):
        pass

class ULC(Service):

	def execute(self,msg):
		if msg.cmd == 'cls':
			print("soy un cls")
			os.system('clear')

		if msg.cmd == 'help':
			print("\n\tCommand : Description")
			for command in cmdDic.keys(): 
				print("\t"+ command + " : " + str(cmdDic[command]))
			print("\n")

		if msg.cmd == 'makedir':
			#Obtener los argumentos del mensaje
			if args != None:
				os.mkdir(name,0o777)
			else:
				print("Invalid arguments were given.")

		if msg.cmd == 'rmdir':
			#Obtener los argumentos del mensaje
			if args != None:
				shutil.rmtree(args, ignore_errors=False, onerror=None)

		if msg.cmd == 'makefile':
			if args != None:
				os.mknod(args,0o600,stat.S_IRUSR)
			else:
				print("Invalid arguments were given.")

		if msg.cmd == 'rmfile':
			if args != None:
				os.remove(args)
			else:
				print("Invalid arguments were given.")

		if msg.cmd == 'li':
			items = os.listdir(".")
			print("\nFiles:")
			for item in items:
				print("\t"+item)
			print("\n")

		if msg.cmd == 'cd':
			if args != None:
				if arg == '..':
					path = os.getcwd().rsplit("/",1)[0]
					os.chdir(path)
					#Evitar que home suba y crashee
				else:
					os.chdir(os.getcwd() + "/" + arg)
					#Evitar que crhasee hacia adelante cuando no existe carpeta o archivo
		if msg.cmd == 'cwd':
			print(os.getcwd())

class SLC(Service):

	def execute(self,msg):
		print("Executing SLC")

class CLC(Service):

	def execute(self,msg):
		print("Executing CLC / " + msg.cmd)
