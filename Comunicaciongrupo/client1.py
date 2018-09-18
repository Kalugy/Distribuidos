import socket
import sys

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
puerto=9900
s.connect(('localhost', puerto))

fin=False
while(fin==False):
	print 'Bienvenido al comunicador de grupos \n 1. crear grupo \n 2. Asignar grupo \n 3. Mostrar grupo \n 4. Eliminar grupo'
	numero1=raw_input("Ingrese numero de 1 a 4: ")
	#Recibe el numero y lo envia al socket conectado
	dato=str('localhost') +' '+ str(puerto) +' '+ str(numero1)
	s.send(dato)
	respuesta=s.recv(1024)
	print "La operacion es : ", respuesta
	if(numero1==5):
		fin=True

s.close()

"""
#mensaje en el cliente
fin=False
while(fin==False):
	
	
	socket1.send(dato)
	if(numero1==5):
		fin=True
"""