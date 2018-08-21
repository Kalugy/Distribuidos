import SocketServer
import math
def logaritmo(numero1, numero2):
	return math.log(numero1,numero2)

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

		self.respuesta = str(logaritmo(float(self.palabra1), float(self.palabra3)))
		print 'los numeros recibidos son: ' , self.palabra1, 'y', self.palabra3, 'y la logaritmo', self.respuesta
		self.request.send(self.respuesta)

def main():
	print 'Logaritmo socket'
	host1='localhost'
	puerto1 = 8500 #Entre 0 y 1000, por los 9000 no estan usando

	socketsuma = SocketServer.TCPServer((host1,puerto1),miHandler)
	socketsuma.serve_forever()

main()
