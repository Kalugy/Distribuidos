import socket
import sys
import thread
import math
from numpy import array
from numpy import *

import time
import datetime
from datetime import datetime as dt
import time

import threading #libreria para el manejo de hilos

#para contador interno del client
from datetime import datetime
formato = "%H:%M:%S"

#SERVER




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 7043))
s.listen(10)

def prender(puerto):
	#conexion al CLIENT1
	s1 = socket.socket()
	s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	s1.connect(('localhost', int(puerto)))

	print "hola estoy prendiendolo" 
	s1.send("0")
	Aquiestalahora1=s1.recv(1024)
	print "aca esta la hora" 
	print Aquiestalahora1
	return Aquiestalahora1
	

def sacapromedio(array):

	lon=len(array)
	varhor=0
	varminutos=0
	varsegundos=0
	nuevahora=array[0]
	if (lon==1):
		print "Solo existe un dato"
		return nuevahora

	else:	
		for hora in array:
			hhmmss=datetime.strptime(hora,formato)
			horas=hhmmss.hour
			minutos = hhmmss.minute
			segundos = hhmmss.second
			
			varhor=horas+varhor
			varminutos=minutos+varminutos
			varsegundos=segundos+varsegundos

			


	        #hhmmss=str(horas)+":"+str(minutos)+":"+str(segundos)


	if(lon>=2):        
		varhor=varhor/lon
		varsegundos=varsegundos/lon
		varminutos=varminutos/lon
		
		nuevahora=str(varhor)+":"+str(varminutos)+":"+str(varsegundos)
		return nuevahora


#Declaracion de Clase
class Hilo(threading.Thread):
    def __init__(self,dato):
#llamando al constructor de la clase Thread y mandando como paramemtro
#la referencia a la clase Hilo
        threading.Thread.__init__(self);
        self.dato= dato;
#metodo que ejecutara el hilo al llamarse con el metodo start()
    def run(self):
        print "Soy el hilo ",self.dato;
        hhmmss=dato

        hhmmss=datetime.strptime(hhmmss,formato)
        horas=hhmmss.hour
        minutos = hhmmss.minute
        segundos = hhmmss.second
        time.sleep(1)
        segundos=segundos+1
        if(segundos==60):
        	segundos=00

        	minutos=minutos+1
        elif(horas==24):
			horas=00	
        elif(minutos==60):
        	minutos=00
        	horas=horas+1
        hhmmss=str(horas)+":"+str(minutos)+":"+str(segundos)
        
        print hhmmss
        print "help"


array=[]
def connection(sc, addr):

	while True:
		puerto=str(sc.recv(1024))
		
		print "Ah escuchado un dato"
		jj=prender(puerto)
		array.append(jj)
		print array

		averaguehour=sacapromedio(array)

		print "aca esta el averaguehour"
		print averaguehour

		#print "Start : %s" % time.ctime()
		#time.sleep( 5 )
		#print "End : %s" % time.ctime()	

		
		print "acamesalideprender"
		sc.send("prendido")





print "respondiendo..."

while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc,addr))



sc.close()
s.close()
s1.close()