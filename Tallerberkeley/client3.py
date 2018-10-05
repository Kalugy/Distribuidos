import socket
import sys
import thread
#!/usr/bin/python
import threading
import Queue
from threading import Thread
import time
import datetime

#para contador interno del client
from datetime import datetime
formato = "%H:%M:%S"



#termina
print "termina"

#conexion al server
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
puerto=7042
puerto2="11179	"
s.connect(('localhost', puerto))




print 'Bienvenido al client con algoritmo berkeley'

dato="11:40:10"

import threading #libreria para el manejo de hilos
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







"""
ho=0
def timess(a):
	
	if(a==0):
		ho=actualizar(dato)
		print ho
		
	elif(a==1):
		ho=actualizar(ho)
		print ho

	
	return ho	

horaactual=timess(0)
def horaahora():

	
	horaactual=timess(1)
	
	return horaactual	



#timess(9,0)
#j=timess(188,1)
#print j
"""

"""
#t.join(); #Espera a que todos los hilos terminen para que finalice el hilo principal

def sumar():
	g=1+1
	print threading.currentThread().getName(), 'Deteniendo'
	print g
	return g

g = threading.Thread(target=sumar)
g.start()
"""
#SERVIDOR
def foo(bar):
	dato=bar
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
	return hhmmss 

que = Queue.Queue()

i=0
h=True
result="11:40:10"


s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s1.bind(('', int(puerto2)))
s1.listen(10)

def actualizar(num,result,h):
	
	while h==True:
		
		while num<10 or num==666666:
			
			t = Thread(target=lambda q, arg1: q.put(foo(arg1)), args=(que, result))
			t.start()
			t.join()
			result = que.get()
			print "ALOALO"
			print result
			num+=1

		print "aca me sali"
		print result	
		h=False	
	return result


def connection(sc1, addr1):
	i=0
	h=True
	while True:
		
		#mirar por que no devuelve el int 
		num=int(sc1.recv(1024))
		

		print num
		

		result="11:40:10"
		hor=actualizar(num,result,h)
		h=False

		print "aca me saliiiiiiiiiiiiiiiiii"
		print hor

		sc1.send(hor)

		respuesta=s.recv(1024)

		print "received"
		print respuesta	





print "respondiendo CLIENT 1..."
s.send(puerto2)
print "enviando"


while 1:

    sc1, addr1 = s1.accept()
    print "recibida conexion de la IP: " + str(addr1[0]) + "puerto: " + str(addr1[1])
    print "\n"
    thread.start_new_thread(connection,(sc1,addr1))




sc1.close()
s1.close()
s.close()