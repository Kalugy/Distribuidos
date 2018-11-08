import socket
import sys
from numpy import *
from numpy import array
import re

def menu():
	print "Calculadora"
	num1=raw_input( "Degite el primer numero: ")
	op=raw_input( "escoja la operacion: ")
	num2=raw_input( "Degite el segundo numero: ")
	dato=str(num1) + "?" + str(op) + "?" + str(num2)
	return dato


def conection(ip, port):
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.connect((ip, port))
	dato=menu()
	s.send(dato)
	respuesta=s.recv(1024)
	print (respuesta)
	s.close()

def main():
	ip,port=pregunta()
	conection(ip,port)

def pregunta():
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.connect(('localhost', 9989))
	s.send("hola")
	respuesta=s.recv(1024)
	ip=respuesta.split("?")[0]
	port=respuesta.split("?")[1]
	s.close()

	return ip,port
	
main()




