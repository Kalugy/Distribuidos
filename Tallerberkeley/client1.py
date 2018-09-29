import socket
import sys
import thread
#!/usr/bin/python
import threading

import time
import datetime

#para contador interno del client
from datetime import datetime
formato = "%H:%M:%S"


#


#conexion al server
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
puerto=7001
puerto2="11090"
s.connect(('localhost', puerto))




print 'Bienvenido al server con algoritmo berkeley'


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

dato="11:54:10"


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
hilo = threading.Thread(target=timess)
hilo.start()
print "ah iniciado"
print hilo


"""
def sumar():
	g=1+1
	print threading.currentThread().getName(), 'Deteniendo'
	print g
	return g

g = threading.Thread(target=sumar)
g.start()
"""
#SERVIDOR

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s1.bind(('', int(puerto2)))
s1.listen(10)

def connection(sc1, addr1):
	num=True
	while True:
		
		
		while num:
			num=str(sc1.recv(1024))
			horanow=horaahora()

		sc1.send("enviando de client a server ok")

		respuesta=s.recv(1024)
		print "received"



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