import socket
import sys
import thread
from time import sleep
#al momento de enviar dos datos al servidor debe esperar este tiempo:
SLEEP_TIME = 0.1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9883))
s.listen(10)

def nuevosocket(puerto,palabra1,palabra3):
	s1 = socket.socket()
	s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s1.connect(('localhost', puerto))

	s1.send(palabra1)
	sleep(SLEEP_TIME)
	s1.send(palabra3)
	respuesta = s1.recv(1024)
	s1.close()
	return respuesta

def connection(sc, addr):

	num=str(sc.recv(1024))

	palabra1=""
	palabra2=""
	palabra3=""
	cuenta = 0
	contador=0

	for carac in num:
		if carac == ' ':
			cuenta+=1
		else:
		   contador+=1
		   if cuenta==0:
			   palabra1+=carac
		   if cuenta==1:
			   palabra2+=carac
		   if cuenta==2:
			   palabra3+=carac

	if(palabra2 == 'suma' or palabra2 == '+'):
		respuesta = (nuevosocket(6000, palabra1, palabra3))

	if(palabra2 == 'resta' or palabra2 == '-'):
		respuesta = (nuevosocket(6500, palabra1, palabra3))

	if(palabra2 == 'multiplicar' or palabra2 == '*'):
		respuesta = (nuevosocket(7000, palabra1, palabra3))

	if(palabra2 == 'dividir' or palabra2 == '/'):
		respuesta = (nuevosocket(7500, palabra1, palabra3))

	if(palabra2 == 'potencia' or palabra2 == '^'):
		respuesta = (nuevosocket(8000, palabra1, palabra3))

	if(palabra2 == 'logaritmo'):
		respuesta = (nuevosocket(8500, palabra1, palabra3))

	if(palabra2 == 'radicacion'):
		respuesta = (nuevosocket(9000, palabra1, palabra3))

	sc.send(respuesta)


print "respondiendo..."

while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc,addr))

sc.close()
s.close()
s1.close()
