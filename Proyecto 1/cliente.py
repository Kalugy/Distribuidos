import socket
import sys
from numpy import *
from numpy import array
import re

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
puerto=9987
s.connect(('localhost', puerto))




def arreglo( disponible, ids, ip,memoria,cpu, port):
	lista={}
	lista['disponible']=disponible
	lista['ids']=ids
	lista['port']=port
	lista['ip']=ip
	lista['memoria']=memoria
	lista['cpu']=cpu
	
	return lista

def asignar(array):
	servidor1=arreglo(1, 1,puerto,'localhost',3,44)
	servidor2=arreglo(0, 2,puerto,"201.131.91.24",5,4)
	array['servidor1']=servidor1
	array['servidor2']=servidor2

def menu():
	print "Calculadora"
	num1=raw_input( "Degite el primer numero: ")
	op=raw_input( "escoja la operacion: ")
	num2=raw_input( "Degite el segundo numero: ")
	dato=str(num1) + "?" + str(op) + "?" + str(num2)
	s.send(dato)


def comprobar(array):
	cont=1
	for servidor in array:
		servidor= array.get("servidor" + str(cont))
		print servidor["ids"]
		if servidor["disponible"] == 0:
			print "entro"
		cont=cont+1
	
	

def main():
	array={}
	asignar(array)
	comprobar(array)
	menu()
	respuesta=s.recv(1024)
	print (respuesta)

main()

s.close()
