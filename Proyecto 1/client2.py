import socket
import sys
from numpy import *
from numpy import array
import re


clientport= 9930

def menu():
	print "Bienvenido"
	print "1. Calculadora"
	print "2. Concatena palabras"
	print "3. busca numero mayor"

	numero=raw_input( "Digite opcion: ")

	
	if numero=='1': 
		num1=raw_input( "Degite el primer numero: ")
		op=raw_input( "escoja la operacion: ")
		num2=raw_input( "Degite el segundo numero: ")
		dato=str(num1) + "?" + str(op) + "?" + str(num2)+ "?"+"oper"
			
	elif numero=='2':
		num1=raw_input( "Digite la primera palabra: ")
		num2=raw_input( "Digite la segundo palabra: ")	
		dato=str(num1) + "?"  + str(num2)+ "?"+"conca" +"?"+"c" 
			
	elif numero=='3':
		num1=raw_input( "Digite el primer numero: ")
		num2=raw_input( "Digite el segundo numero: ")	
		num3=raw_input( "Digite el tercer numero: ")
		num4=raw_input( "Digite el cuarto numero: ")
		num5=raw_input( "Digite el quinto numero: ")
		dato=str(num1) + "?"  + str(num2)+ "?"+str(num3)+ "?"+str(num4)+"?"+str(num5)+"?"+ "mayor"
			
	else :
		print "por favor numero dentro de rango"
		dato="0"
		
	
	return dato


def conection(ip, port):
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.connect((ip, int(port)))
	dato=menu()
	print "paso"
	s.send(dato)
	respuesta=s.recv(1024)
	print "El resultado de la operacion es : ", respuesta
	s.close()



def pregunta():
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.connect(('localhost', clientport))
	s.send("hola")
	respuesta=s.recv(1024)
	ip=respuesta.split("?")[0]
	port=respuesta.split("?")[1]
	s.close()
	print "final",ip, port
	return ip,port
	

def main():
	ip,port=pregunta()
	conection(ip,port)

main()





