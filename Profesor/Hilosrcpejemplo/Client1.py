from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
import time

def div(x, y):
	return x // y

class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):
    def __init__(self):
         threading.Thread.__init__(self)
         self.localServer = SimpleThreadedXMLRPCServer(("localhost",10012))
         self.localServer.register_function(div)

    def run(self):
         self.localServer.serve_forever()

server = ServerThread()
server.start() # The server is now running
print "Listo servidor."

class ClientThread(threading.Thread):
    def __init__(self):
		threading.Thread.__init__(self)
		self.s = xmlrpclib.ServerProxy('http://localhost:10011')

    def run(self):
		time.sleep(3)
		print "Llamada cliente"
		print self.s.div(5,2)  # Returns 5//2 = 2

client = ClientThread()
client.start() # The server is now running
