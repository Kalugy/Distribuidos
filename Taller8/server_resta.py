import socket
import sys
import thread
import math

def resta(numero1, numero2):
	return numero1-numero2


s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind(('', 6500))
s1.listen(10)

def connection(sc, addr):

	num1=str(sc1.recv(1024))
	num2=str(sc1.recv(1024))

	respuesta=str(resta(float(num1),float(num2)))
	print 'los numeros recibidos son: ', num1, ' y ', num2, 'y la resta ', respuesta

	sc1.send(respuesta)


print "respondiendo..."

while 1:

    sc1, addr = s1.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc1,addr))

sc1.close()
s1.close()
