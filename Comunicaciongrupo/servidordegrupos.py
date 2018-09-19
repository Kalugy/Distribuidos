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

s.bind(('', 9935	))
s.listen(10)



def connection(sc, addr):

	num=str(sc.recv(1024))
	resulta=""
	palabra1=""
	palabra2=""
	palabra3=""
	palabra4=""
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
		   if cuenta==3:
			   palabra4+=carac

	if(palabra3 == '1' ):
		
		#creacion de grupos
		lineas = len(open('BD.txt').readlines())
		print lineas

		if(lineas==0):
			p= 'Grupo 1' +' '+ palabra1 +' ' +str(addr[1])
			f = open ('BD.txt','w')
			f.write(p)
			f.close()
			resulta="Crea nuevo grupo"
		elif(lineas>0):
			lineas1=lineas+1
			p= '\nGrupo ' + str(lineas1) + ' '+ palabra1 +' ' +str(addr[1]) 
			f = open ('BD.txt','a')
			f.write(str(p))
			f.close()
			resulta="Creacion de grupo"
		
	#Asigna gente a un grupo
	elif(palabra3 == '2' ):
		print "hola "
		print palabra4+"  "
		# abrimos el archivo solo de lectura
		f = open("BD.txt","r")
		 
		# Creamos una lista con cada una de sus lineas
		lineas = f.readlines()
		cantidaddegrupos= len(lineas)
		print lineas
		# cerramos el archivo
		f.close()
		if cantidaddegrupos==0:
			print "no existen grupos"
		else:	
			# abrimos el archivo pero vacio
			f = open("BD.txt","w")
			a=1
			# recorremos todas las lineas expeto la ultima que es la que borramos
			
			for linea in lineas:
				if(a==int(palabra4)):
					print "agregando"+ linea
					resulta="agregando un nuevo miembro al grupo"
					data1= linea.replace("\n", "")
					data=data1+' '+palabra1+' '+str(addr[1]) 
					f.write(data + "\n")
					a=a+1					
					#f.write(str(data))
					
				elif(a<=cantidaddegrupos):
					f.write(linea)
					a=a+1
				else:
					print "grupo no existe"    

			    
			# cerramos el archivo
			f.close()



	#muestra los grupos
	elif(palabra3 == '3' ):
		

		f = open ('BD.txt','r')
		mensaje=f.read()
		print (mensaje)
		f.close()
		resulta="Mostrando elementos"
	#un pequeño bug cuando borro todos los elementos, tambien cuando agrego un host y luego
	#intento crear un otro grupo, hay un salto de linea que me crea solo aca en eliminar
	#siempre elimina el ultimo grupo de la lista
	elif(palabra3 == '4' ):
		# abrimos el archivo solo de lectura
		f = open("BD.txt","r")
		 
		# Creamos una lista con cada una de sus lineas
		lineas = f.readlines()
		cantidaddegrupos= len(lineas)
		# cerramos el archivo
		f.close()
		if cantidaddegrupos==0:
			print "no existen grupos"
		else:	
			# abrimos el archivo pero vacio
			f = open("BD.txt","w")
			a=1
			# recorremos todas las lineas expeto la ultima que es la que borramos
			
			for linea in lineas:
				if(a<cantidaddegrupos):
					f.write(linea)
					a=a+1
					print a
					resulta="borrado el ultimo elemento"

			 	
			# cerramos el archivo
			f.close()


		

	sc.send(resulta)





print "respondiendo..."

while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc,addr))

sc.close()
s.close()
