import Queue
from threading import Thread
import time

import datetime

#para contador interno del client
#contador con hilos y funcion 
from datetime import datetime
formato = "%H:%M:%S"

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
result="11:54:10"
while h==True:
	
	while i<10 or i==666666:
		
		t = Thread(target=lambda q, arg1: q.put(foo(arg1)), args=(que, result))
		t.start()
		t.join()
		result = que.get()
		print "ALOALO"
		print result
		i+=1
		print i

	print "aca me sali"
	print result	
	h=False	
	