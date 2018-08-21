import SocketServer

def dividir(numero1, numero2):
	return numero1/numero2

class miHandler(SocketServer.BaseRequestHandler):

	def handle(self):

		

		self.numero1 = self.request.recv(1024)
		self.numero2 = self.request.recv(1024)

		self.division = str(dividir(float(self.numero1), float(self.numero2)))
		print 'los numeros recibidos son: ' , self.numero1, 'y', self.numero2, 'y la division es: ', self.division
		self.request.send(self.division)

def main():
	print 'Division socket'
	host1='localhost'
	puerto1 = 7500 #Entre 0 y 1000, por los 9000 no estan usando

	socketsuma = SocketServer.TCPServer((host1,puerto1),miHandler)
	socketsuma.serve_forever()

main()