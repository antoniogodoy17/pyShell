import threading
import time
import logging
import Queue
import socket
import time
from message import Message
from service import ULC,SLC,CLC

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

#Queue size
qSize = 10

#Global queue (shared memory)
q = Queue.Queue(qSize)

#Conditional Variable 
cv = threading.Condition()

class Coordinator:
    def __init__(self):
        self.queue = q
        self.cv = cv

    def communicator(self):
        #Create the server socket object -> socket.socket()
        #AF_INET address family
        #SOCK_STREAM socket type (STREAM is quick and usefull)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Get local machine name
        self.host = '127.0.0.1'#socket.gethostname()
        #Declare the port
        self.port = 9000
        #Bind socket to the port -> socket.bind(address)
        self.s.bind((self.host,self.port))
        #Specify how many requests will listen at the same time (queue) -> socket.listen(backlog), min=0, max=5 (system dependent)
        self.s.listen(5)
        logging.debug("Server Started.\n")

        while True:
            #Establish connection -> socket.accept() retunrs a pair value (conn,address) where conn is a new socket object (to send and recieve data on the connection) and address is the adress bound to the socket on the other end of the connection.
            #.accept() creates a new socket used to communicate with it. In TCP servers, this is not the case, the socket created here is only used to returns a new socket.
            (clientSocket,addr) = self.s.accept()
            logging.debug("Client connected: %s." %str(addr))
            
            while True:
                msgRecv = clientSocket.recv(1024)
                if not msgRecv: 
                    break
                logging.debug("Message Received From %s." %str(addr))
                message = Message()
                message = message.marshal(msgRecv)
                if not self.queue.full():
                    self.cv.acquire()
                    self.put(message)
                    self.cv.notify()
                    self.cv.release()
            
            #Close the connection -> socket.close(), mark the socket closed, all future operations on the socket object will fail.
            clientSocket.close()

    def coordinator(self):
        while True:
            self.cv.acquire()
            while self.queue.empty():
                self.cv.wait()
            msg = self.get()
            self.cv.release()
            logging.debug('Command Received: %s' %str(msg.cmd))
            #
            if msg.type == "user":
                uCmd = ULC()
                uCmd.execute(msg)

            elif msg.type == "system":
                sCmd = SLC()
                sCmd.execute(msg)

            else: #Type = "Control"
                cCmd = CLC()
                cCmd.execute(msg)

    def put(self,msg):
        logging.debug('Putting command: %s' %str(msg.cmd))
        self.queue.put(msg)

    def get(self):
        msg = self.queue.get()
        logging.debug('Getting command: %s' %str(msg.cmd))
        return msg 

    def run(self,name,who):
        t = threading.Thread(name=name,target=who)
        t.start()

if __name__ == '__main__':
    comm = Coordinator()
    comm.run("Communicator",comm.communicator)
    coord = Coordinator()
    coord.run("Coordinator",comm.coordinator)