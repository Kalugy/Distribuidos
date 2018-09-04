import socket
import sys
import thread
import math

def suma(numero1, numero2):
	return numero1+numero2
def resta(numero1, numero2):
	return numero1-numero2
def multiplicar(numero1, numero2):
	return numero1*numero2
def dividir(numero1, numero2):
	return numero1/numero2
def potencia(numero1, numero2):
	return numero1**numero2
def logaritmo(numero1, numero2):
	return math.log(numero1,numero2)
def radicacion(numero1, numero2):
	return math.pow(numero1,numero2)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 9882))
s.listen(10)

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
		respuesta=str(suma(int(palabra1),int(palabra3)))
		print 'los numeros recibidos son: ', palabra1, ' y ', palabra3, 'y la suma ', respuesta

	if(palabra2 == 'resta' or palabra2 == '-'):
		respuesta=str(resta(int(palabra1),int(palabra3)))
		print 'los numeros recibidos son: ', palabra1, ' y ', palabra3, 'y la resta ', respuesta

	if(palabra2 == 'multiplicar' or palabra2 == '*'):
		respuesta=str(multiplicar(int(palabra1),int(palabra3)))
		print 'los numeros recibidos son: ', palabra1, ' y ', palabra3, 'y la multiplicacion es ', respuesta

	if(palabra2 == 'dividir' or palabra2 == '/'):
		respuesta=str(dividir(int(palabra1),int(palabra3)))
		print 'los numeros recibidos son: ', palabra1, ' y ', palabra3, 'y la dividir es ', respuesta

	if(palabra2 == 'potencia' or palabra2 == '^'):
		respuesta=str(potencia(int(palabra1),int(palabra3)))
		print 'los numeros recibidos son: ', palabra1, ' y ', palabra3, 'y la dividir es ', respuesta
	if(palabra2 == 'logaritmo'):
		respuesta=str(logaritmo(int(palabra1),int(palabra3)))
		print 'los numeros recibidos son: ', palabra1, ' y ', palabra3, 'y la dividir es ', respuesta

	if(palabra2 == 'radicacion'):
		respuesta=str(radicacion(float(palabra1),float(palabra3)))
		print 'los numeros recibidos son: ', palabra1, ' y ', palabra3, 'y la dividir es ', respuesta

	sc.send(respuesta)


print "respondiendo..."

while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc,addr))

sc.close()
s.close()
