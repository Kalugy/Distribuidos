import SocketServer
import socket
import math
from time import sleep
from numpy import array
from numpy import *
#al momento de enviar dos datos al servidor debe esperar este tiempo:
SLEEP_TIME = 0.00001

#creacion de sockets para la conexion
def nuevosocket(host_name,puerto,palabra1,palabra3):
	respuesta = ""
	host1 =host_name
	puerto1=puerto
	socket_name=socket.socket()
	socket_name.connect((host1,puerto1))
	socket_name.send(palabra1)
	sleep(SLEEP_TIME)
	socket_name.send(palabra3)
	respuesta = socket_name.recv(1024)
	socket_name.close()
	return respuesta

class miHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		#Recibe el num del cliente
		self.num=str(self.request.recv(1024))
		#defincion de variables locales
		self.palabra1=""
		self.palabra2=""
		self.palabra3=""
		self.a=0;
		
		self.cuenta=0
		self.contador=0
		#cuando cuantas veces esta un signo dentro de la palabra y las separa segun la cantidad de signos
		for carac in self.num:
		    if carac == ' ':
				self.cuenta+=1
		    else:
			   self.contador+=1
			   if self.cuenta==0:
				   self.palabra1+=carac
			   if self.cuenta==1:
				   self.palabra2+=carac
			   if self.cuenta==2:
				   self.palabra3+=carac
		#print "este es el contador",self.contador
		#Recitifcamos que divida bien las palabras
		print "word1",self.palabra1
		print "word2",self.palabra2
		print "word3",self.palabra3
		#dependiendo la operacion (palabra3) entrara al if
		if(self.palabra3 == '1' ):
			self.a+=1
			Grupo='grupo '+str(self.a)
			
			array=[Grupo,[" "," "]]
		
			print (array)


		elif(self.palabra3 == '2' ):
			pass
	
		else:
			print 'No exite la operacion, servidor de la operacion no encontrado, por favor digite nuevamente'
		#mensaje del server
		#print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la ',self.palabra2 ,' es ' , self.respuesta
		#self.request.send(self.respuesta)

def main():
		print 'Server mediador'
		host= 'localhost'
		puerto= 9512
		server1=SocketServer.TCPServer((host,puerto),miHandler)
		print "server corriendo"
		server1.serve_forever()

main()
