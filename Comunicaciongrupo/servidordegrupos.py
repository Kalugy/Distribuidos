import socket
import sys
import thread
import math
from numpy import array
from numpy import *

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

s.bind(('', 9900	))
s.listen(10)


def nuevogrupo(grupo):
	grupo=[grupo,[" "," "]]
	return grupo

def connection(sc, addr):

	num=str(sc.recv(1024))

	palabra1=""
	palabra2=""
	palabra3=""
	cuenta = 0
	contador=0
	a=0


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

	if(palabra3 == '1' ):
		
		lineas = len(open('BD.txt').readlines())
		print lineas

		if(lineas==0):
			p= 'Grupo 0' +' '+ palabra1 +' ' +str(addr[1])
			f = open ('BD.txt','w')
			f.write(p)
			f.close()
		elif(lineas>0):
			p= 'Grupo ' + str(lineas) + ' '+ palabra1 +' ' +str(addr[1]) 
			f = open ('BD.txt','a')
			f.write('\n' + str(p))
			f.close()
		
		
	elif(palabra3 == '3' ):
		

		f = open ('BD.txt','r')
		mensaje=f.read()
		print (mensaje)
		f.close()
	elif(palabra3 == '4' ):
		# abrimos el archivo solo de lectura
		f = open("BD.txt","r")
		 
		# Creamos una lista con cada una de sus lineas
		lineas = f.readlines()
		 
		# cerramos el archivo
		f.close()
		 
		# abrimos el archivo pero vacio
		f = open("BD.txt","w")
		 
		# recorremos todas las lineas
		for linea in lineas:
		    if linea!="linea 4"+"\n":
		        f.write(linea)
		 
		# cerramos el archivo
		f.close()

		

	sc.send(str(addr[1]))





print "respondiendo..."

while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc,addr))

sc.close()
s.close()
