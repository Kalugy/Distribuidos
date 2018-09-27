import socket
import sys

#!/usr/bin/python


import time
import datetime

#para contador interno del client
from datetime import datetime
formato = "%H:%M:%S"

#conexion al server
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
puerto=9992
s.connect(('localhost', puerto))


print 'Bienvenido al server con algoritmo cristian '


#contar segundos 
def actualizar (dato):

	hhmmss=dato

	#print "Start : %s" % time.ctime()
	#time.sleep( 5 )
	#print "End : %s" % time.ctime()
	
	hhmmss = datetime.strptime(hhmmss, formato)
	horas = hhmmss.hour
	minutos = hhmmss.minute
	segundos = hhmmss.second


	time.sleep(1)
	segundos=segundos+1
	if(segundos==60):
		segundos=00
		minutos=minutos+1
	elif(minutos==60):
		minutos=00
		horas=horas+1
	elif(horas==24):
		horas=00
					


	hhmmss= str(horas)+':'+str(minutos)+':'+str(segundos)
	dato=hhmmss
	return hhmmss

dato="12:54:10"
a=0

#cada 5 segundos rectificamos el tiempo con el server
while True:
	
	if(a==0):
		ho=actualizar(dato)
		print ho
		a+=1
	elif(a<=5):
		ho=actualizar(ho)
		print ho
		a+=1
	else:
		s.send(ho)
		a=1
		print 'mensaje enviado'
		respuesta=s.recv(1024)
		
		ho=respuesta
	
 
	
	
s.close()

