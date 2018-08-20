import SocketServer
import math
def logaritmo(numero1, numero2):
	return math.log(numero1,numero2)

class miHandler(SocketServer.BaseRequestHandler):

	def handle(self):

		self.numero1 = self.request.recv(1024)
		self.numero2 = self.request.recv(1024)

		self.respuesta = str(logaritmo(float(self.numero1), float(self.numero2)))
		print 'los numeros recibidos son: ' , self.numero1, 'y', self.numero2, 'y la logaritmo', self.respuesta
		self.request.send(self.respuesta)

def main():
	print 'Logaritmo socket'
	host1='localhost'
	puerto1 = 8502 #Entre 0 y 1000, por los 9000 no estan usando

	socketsuma = SocketServer.TCPServer((host1,puerto1),miHandler)
	socketsuma.serve_forever()

main()
