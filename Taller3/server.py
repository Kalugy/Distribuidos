import SocketServer
import socket
import math
from time import sleep
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
		print "aca cuantas veces encontro el signo",self.cuenta
		#dependiendo la operacion (palabra2) entrara al if
		if(self.palabra2 == 'suma' or self.palabra2 == '+'):
			self.request.send('localhost')
			sleep(SLEEP_TIME)
			self.request.send('6002')

		elif(self.palabra2 == 'resta' or self.palabra2 == '-'):
			self.request.send('localhost')
			sleep(SLEEP_TIME)
			self.request.send('6500')

		elif(self.palabra2 == 'multiplicar' or self.palabra2 == '*'):
			self.request.send('localhost')
			sleep(SLEEP_TIME)
			self.request.send('7000')
			
		elif(self.palabra2 == 'dividir' or self.palabra2 == '/'):
			self.request.send('localhost')
			sleep(SLEEP_TIME)
			self.request.send('7500')
			
		elif(self.palabra2 == 'potencia' or self.palabra2 == '^'):
			self.request.send('localhost')
			sleep(SLEEP_TIME)
			self.request.send('8000')
			
		elif(self.palabra2 == 'logaritmo'):
			self.request.send('localhost')
			sleep(SLEEP_TIME)
			self.request.send('8500')
			
		elif(self.palabra2 == 'radicacion'):
			self.request.send('localhost')
			sleep(SLEEP_TIME)
			self.request.send('9000')
			
		else:
			print 'No exite la operacion, servidor de la operacion no encontrado, por favor digite nuevamente'
		#mensaje del server
		#print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la ',self.palabra2 ,' es ' , self.respuesta
		#self.request.send(self.respuesta)

def main():
		print 'Server mediador'
		host= 'localhost'
		puerto= 9510
		server1=SocketServer.TCPServer((host,puerto),miHandler)
		print "server corriendo"
		server1.serve_forever()

main()
