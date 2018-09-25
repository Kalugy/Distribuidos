import socket
import sys
import thread
import math
from numpy import array
from numpy import *

import time
import datetime
from datetime import datetime as dt



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 9992))
s.listen(10)


def actualizarhora():
	
	
	
	t = dt.now()
	horactual=t.hour

	return horactual

def actualizarminuto():

	t = dt.now()
	
	minutosactual=t.minute

	return minutosactual

def actualizarseg():	
	t = dt.now()

	segundosactual = t.second
	
	return segundosactual

from datetime import datetime
formato = "%H:%M:%S"

def connection(sc, addr):

	while True:
		num=str(sc.recv(1024))
		

		hhmmss = num
		#if hhmmss == "":
		
		hhmmss = datetime.strptime(hhmmss, formato)
		horas = hhmmss.hour
		minutos = hhmmss.minute
		segundos = hhmmss.second
		#hhmmss_seg = (horas * 60 * 60) + (minutos * 60) + segundos 
		#resultado = float(hhmmss_seg / 86400)
		
		
		
		horactual=actualizarhora()
		minutosactual=actualizarminuto()
		segundosactual=actualizarseg()
		#segundosactual=int(segundosactual)+1
		resultado=num
		print "alo"
		print (str(segundosactual)) 
		print (str(segundos))

		if(segundosactual!=segundos):
			#if para pasar de segundos en el formato (cuando es mayor)
			if segundosactual>=45 and segundos<30:
				#if para rectificar los 15 segundos
				if(segundos<15):
					#verifica minutos del formato
					if minutosactual==minutos:
						pass
					else:
						if segundosactual==59:
							segundosactual=00
							resultado=str(horactual)+':'+str(minutosactual)+':'+str(segundosactual)
						else:	
							resultado=str(horactual)+':'+str(minutosactual)+':'+str(segundosactual)
				else:
					resultado=str(horactual)+':'+str(minutosactual)+':'+str(segundosactual)
			#caso para cuando segundos es mayor a 15 segundos 		
			elif segundos>=45 and segundosactual<30:
				#if para rectificar los 15 segundos
				if(segundosactual<15):
					#verifica minutos del formato
					if minutos==minutosactual:
						pass
					else:
						resultado=str(horactual)+':'+str(minutosactual)+':'+str(segundosactual)
				else:
					resultado=str(horactual)+':'+str(minutosactual)+':'+str(segundosactual)
			#cuando esta en el formato pero hay diferencia de 15 segundos
			else:
				diferencia=segundosactual-segundos
				if diferencia<=15 or diferencia>=-15:
					if minutosactual!=minutos:
						if segundosactual==59:
							segundosactual=00
							resultado=str(horactual)+':'+str(minutosactual)+':'+str(segundosactual)
						else:	
							resultado=str(horactual)+':'+str(minutosactual)+':'+str(segundosactual)
					
					else:
						if horactual!=horas:
							if segundosactual==59:
								segundosactual=00
								resultado=str(horactual)+':'+str(minutosactual)+':'+str(segundosactual)
							else:	
								resultado=str(horactual)+':'+str(minutosactual)+':'+str(segundosactual)
						else:
							pass	


					
				elif diferencia>=15 or diferencia<=-15:
					resultado=str(horactual)+':'+str(minutosactual)+':'+str(segundosactual)
			
		else:

			if segundosactual==59:
				segundosactual=00
				resultado=str(horactual)+':'+str(minutosactual)+':'+str(segundosactual)
			else:	

				resultado=str(horactual)+':'+str(minutosactual)+':'+str(segundosactual)
		
		print "mensaje enviar a cliente" + resultado
		sc.send(resultado)





print "respondiendo..."

while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc,addr))



sc.close()
s.close()
