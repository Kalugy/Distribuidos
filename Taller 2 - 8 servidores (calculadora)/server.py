import SocketServer
import socket
import math
from time import sleep

SLEEP_TIME = 0.1


class miHandler(SocketServer.BaseRequestHandler):
	def handle(self):


		self.num=str(self.request.recv(1024))

		self.longitud=len(self.num)

		self.palabra1=""
		self.palabra2=""
		self.palabra3=""
		self.cuenta = 0
		self.contador=0



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
		print "word1",self.palabra1
		print "word2",self.palabra2
		print "word3",self.palabra3
		print "aca cuantas veces encontro el signo",self.cuenta

		if(self.palabra2 == 'suma' or self.palabra2 == '+'):
			host1 ='localhost'
			puerto1=6000
			socketsuma=socket.socket()
			socketsuma.connect((host1,puerto1))
			
			socketsuma.send(self.palabra1)
			sleep(SLEEP_TIME)
			socketsuma.send(self.palabra3)
			self.respuesta = socketsuma.recv(1024)
			socketsuma.close()

			print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la suma ', self.respuesta

		if(self.palabra2 == 'resta' or self.palabra2 == '-'):
			host1 ='localhost'
			puerto1=6500
			socketresta=socket.socket()
			socketresta.connect((host1,puerto1))
			
			socketresta.send(self.palabra1)
			sleep(SLEEP_TIME)
			socketresta.send(self.palabra3)
			self.respuesta = socketresta.recv(1024)
			socketresta.close()

			print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la resta ', self.respuesta

		if(self.palabra2 == 'multiplicar' or self.palabra2 == '*'):
			host1 ='localhost'
			puerto1=7000
			socketmultiplicacion=socket.socket()
			socketmultiplicacion.connect((host1,puerto1))
			
			socketmultiplicacion.send(self.palabra1)
			sleep(SLEEP_TIME)
			socketmultiplicacion.send(self.palabra3)
			self.respuesta = socketmultiplicacion.recv(1024)
			socketmultiplicacion.close()

			print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la multiplicacion es ', self.respuesta

		if(self.palabra2 == 'dividir' or self.palabra2 == '/'):

			host1 ='localhost'
			puerto1=7500
			socketdividir=socket.socket()
			socketdividir.connect((host1,puerto1))
			
			socketdividir.send(self.palabra1)
			sleep(SLEEP_TIME)
			socketdividir.send(self.palabra3)
			self.respuesta = socketdividir.recv(1024)
			socketdividir.close()

			print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la dividir es ', self.respuesta

		if(self.palabra2 == 'potencia' or self.palabra2 == '^'):

			host1 ='localhost'
			puerto1=8000
			socketpotencia=socket.socket()
			socketpotencia.connect((host1,puerto1))
			
			socketpotencia.send(self.palabra1)
			sleep(SLEEP_TIME)
			socketpotencia.send(self.palabra3)
			self.respuesta = socketpotencia.recv(1024)
			socketpotencia.close()


			print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la potencia es ', self.respuesta
		if(self.palabra2 == 'logaritmo'):

			host1 ='localhost'
			puerto1=8501
			socketlogaritmo=socket.socket()
			socketlogaritmo.connect((host1,puerto1))
			
			socketlogaritmo.send(self.palabra1)
			sleep(SLEEP_TIME)
			socketlogaritmo.send(self.palabra3)
			self.respuesta = socketlogaritmo.recv(1024)
			socketlogaritmo.close()

			print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la logaritmia es ', self.respuesta

		if(self.palabra2 == 'radicacion'):


			host1 ='localhost'
			puerto1=9003
			socketradicacion=socket.socket()
			socketradicacion.connect((host1,puerto1))
			
			socketradicacion.send(self.palabra1)
			sleep(SLEEP_TIME)
			socketradicacion.send(self.palabra3)
			self.respuesta = socketradicacion.recv(1024)
			socketradicacion.close()

			print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la radicacion es ', self.respuesta

		self.request.send(self.respuesta)
		

def main():
		print 'taller-socket'
		host= 'localhost'
		puerto= 9502
		server1=SocketServer.TCPServer((host,puerto),miHandler)
		print "server corriendo"
		server1.serve_forever()

main()
