import socket
import sys

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
puerto=9935
s.connect(('localhost', puerto))


print 'Bienvenido al comunicador de grupos \n 1. crear grupo \n 2. Asignar grupo \n 3. Mostrar grupo \n 4. Eliminar grupo'
numero1=raw_input("Ingrese numero de 1 a 4: ")
#Recibe el numero y lo envia al socket conectado
numero2=0

if (numero1=='2'):
	f = open ('BD.txt','r')
	mensaje=f.read()
	print (mensaje)
	f.close()
	numero2=raw_input("Ingrese el grupo al que desea asignar: ")

elif (numero1=='3'):
	f = open ('BD.txt','r')
	mensaje=f.read()
	print (mensaje)
	f.close()
"""
elif (numero1=='4'):
	f = open ('BD.txt','r')
	mensaje=f.read()
	print (mensaje)
	f.close()
	numero2=raw_input("Ingrese el grupo al que desea eliminar: ")
"""



dato=str('localhost') +' '+ str(puerto) +' '+ str(numero1)+ ' '+ str(numero2) 

s.send(dato)


respuesta=s.recv(1024)
print respuesta


s.close()

"""
#mensaje en el cliente
fin=False
while(fin==False):
	
	
	socket1.send(dato)
	if(numero1==5):
		fin=True
"""