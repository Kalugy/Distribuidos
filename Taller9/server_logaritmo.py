import socket
import sys
import thread
import math

def logaritmo(numero1, numero2):
	return math.log(numero1,numero2)


s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind(('', 8500))
s1.listen(10)

def connection(sc, addr):

	num=str(sc1.recv(1024))
	palabra1=""
	palabra2=""
	palabra3=""
	cuenta=0
	contador=0
	#cuando cuantas veces esta un signo dentro de la palabra y las separa segun la cantidad de signos
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


	suman = str(logaritmo(float(palabra1), float(palabra3)))
	print 'los numeros recibidos son: ' , palabra1, 'y', palabra3, 'y la logaritmo es: ', suman
	sc1.send(suman)


print "respondiendo..."

while 1:

    sc1, addr = s1.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc1,addr))

sc1.close()
s1.close()
