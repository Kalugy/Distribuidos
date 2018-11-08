import socket
import sys
import thread
import math
from numpy import *
from numpy import array


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 9989 ))
s.listen(10)

array={}
def connection(sc, addr):
	num=str(sc.recv(1024))
	if num == "hola":
		print num
		port, ip=comprobar(array)
		sc.send(str(ip) + "?" + str(port))

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
	servidor1=arreglo(0, 1,9987,'localhost',3,44)
	servidor2=arreglo(1, 2,9987,'201.131.91.24',5,4)
	array['servidor1']=servidor1
	array['servidor2']=servidor2


	return array


def comprobar(array):
	cont=1

	for servidor in array:
		servidor= array.get("servidor" + str(cont))
		print servidor["ids"]
		if servidor["disponible"] == 0:
			print "entro"
			port=servidor["port"]
			ip = servidor["ip"] 
			
		cont=cont+1
	
	return port, ip	

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
