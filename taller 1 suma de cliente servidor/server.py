import SocketServer
import math
def suma(numero1, numero2):
	return numero1+numero2
def resta(numero1, numero2):
	return numero1-numero2
def multiplicar(numero1, numero2):
	return numero1*numero2
def dividir(numero1, numero2):
	return numero1/numero2
def potencia(numero1, numero2):
	return numero1**numero2
def logaritmo(numero1, numero2):
	return math.log(numero1,numero2)
def radicacion(numero1, numero2):
	return math.pow(numero1,numero2)

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

		if(self.palabra2 == 'suma'):
			self.respuesta=str(suma(int(self.palabra1),int(self.palabra3)))
			print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la suma ', self.respuesta

		if(self.palabra2 == 'resta'):
			self.respuesta=str(resta(int(self.palabra1),int(self.palabra3)))
			print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la resta ', self.respuesta

		if(self.palabra2 == 'multiplicar'):
			self.respuesta=str(multiplicar(int(self.palabra1),int(self.palabra3)))
			print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la multiplicacion es ', self.respuesta

		if(self.palabra2 == 'dividir'):
			self.respuesta=str(dividir(int(self.palabra1),int(self.palabra3)))
			print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la dividir es ', self.respuesta

		if(self.palabra2 == 'potencia'):
			self.respuesta=str(potencia(int(self.palabra1),int(self.palabra3)))
			print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la dividir es ', self.respuesta
		if(self.palabra2 == 'logaritmo'):
			self.respuesta=str(logaritmo(int(self.palabra1),int(self.palabra3)))
			print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la dividir es ', self.respuesta

		if(self.palabra2 == 'radicacion'):
			self.respuesta=str(radicacion(float(self.palabra1),float(self.palabra3)))
			print 'los numeros recibidos son: ', self.palabra1, ' y ', self.palabra3, 'y la dividir es ', self.respuesta

		self.request.send(self.respuesta)



def main():
		print 'taller-socket'
		host= 'localhost'
		puerto= 9986
		server1=SocketServer.TCPServer((host,puerto),miHandler)
		print "server corriendo"
		server1.serve_forever()

main()
