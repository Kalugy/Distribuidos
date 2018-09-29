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


#SERVER
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 7001))
s.listen(10)

def prender(puerto):
	#conexion al CLIENT1
	s1 = socket.socket()
	s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	s1.connect(('localhost', int(puerto)))

	print "hola estoy prendiendolo" 
	s1.send("False")
	Aquiestalahora1=s1.recv(1024)
	print Aquiestalahora1
	


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
		puerto=str(sc.recv(1024))
		
		print "asdasdacasascasas"
		prender(puerto)
		

		#print "Start : %s" % time.ctime()
		#time.sleep( 5 )
		#print "End : %s" % time.ctime()	

		
	
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