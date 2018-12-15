import socket
import sys
import thread
import math
from numpy import *
from numpy import array


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 9929 ))
s.listen(10)


array={}

def connection(sc, addr):
	while True:
		num=str(sc.recv(1024))
		if num == "hola":
			actualizar(array)
			print num
			port, ip = comprobar(array)
			print port, ip 
			
			sc.send(str(ip) + "?" + str(port))
			asignar(array)


def arreglo( disponible, ids, port, ip,memoria,cpu ):
	lista={}
	lista['disponible']=disponible
	lista['ids']=ids
	lista['port']=port
	lista['ip']=ip
	lista['memoria']=memoria
	lista['cpu']=cpu
	
	return lista

def asignar(array):
	servidor1=arreglo(0, 1,8025,'localhost',3,44)
	array['servidor1']=servidor1


def actualizar(array):
	cont=1
	for servidor in array:
		servidor= array.get("servidor" + str(cont))
		if servidor["ids"] == cont:
			print "actualizo"
			s1 = socket.socket()
			s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s1.connect((servidor["ip"], int(servidor["port"])))
			s1.send("disponible")
			respuesta=s1.recv(1024)
			

			print respuesta

			servidor["disponible"]=respuesta.split("?")[0]
			s.close()
			
		cont=cont+1

	return array


def comprobar(array):
	cont=1
	print array
	for servidor in array:
		servidor= array.get("servidor" + str(cont))
		print servidor["ids"]
		if servidor["disponible"] == '0':
			print "entro"
			puerto=servidor["port"]
			ip1 = servidor["ip"] 
		cont=cont+1
	
	return puerto, ip1	

def main():
	asignar(array)
	




print "respondiendo..."
main()
while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc,addr))

    



sc.close()
s.close()