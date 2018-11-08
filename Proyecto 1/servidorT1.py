import socket
import sys
import thread
import math
from numpy import *
from numpy import array

puerto2 =9950
puertog=9971

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s1.bind(('', puertog))
s1.listen(10)


def connection1(sc1, addr1):
	num=str(sc1.recv(1024))
	if num == "disponible":
		result=memoria()
		sc1.send(str(result) + '?' + str(puerto2))		



def memoria ():
	proceso = 10024
	memoria= 200
	if memoria < proceso:
		return 0

print "respondiendo..."

while 1:

    sc1, addr1 = s1.accept()
    print "recibida conexion de la IP: " + str(addr1[0]) + "puerto: " + str(addr1[1])
    print "\n"
    thread.start_new_thread(connection1,(sc1,addr1))

sc1.close()
s1.close()




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost',  9950 ))
s.listen(10)


def connection(sc, addr):
	num=str(sc.recv(1024))
	print num
	result=calculadora(num)
	sc.send(str(result))

def calculadora(num):
	num1=num.split("?")[0]
	palabra2=num.split("?")[1]
	num2=num.split("?")[2]
	if(palabra2 == 'suma' or palabra2 == '+'):
		resultado= suma(num1,num2)

	elif(palabra2 == 'resta' or palabra2 == '-'):
		resultado= resta(num1,num2)

	elif(palabra2 == 'multiplicar' or palabra2 == '*'):
		resultado= multiplicar(num1,num2)

	elif(palabra2 == 'dividir' or palabra2 == '/'):
		resultado= dividir(num1,num2)

	elif(palabra2 == 'potencia' or palabra2 == '^'):
		resultado= potencia(num1,num2)

	elif(palabra2 == 'logaritmo'):
		resultado= logaritmo(num1,num2)

	elif(palabra2 == 'radicacion'):
		resultado= radicacion(num1,num2)
	return resultado


def suma( x, y):
    return float(x) + float(y)
def resta( x, y):
    return float(x) - float(y)
def multiplicar( x, y):
    return float(x) * float(y)
def dividir( x, y):
    return float(x) / float(y)
def potencia( x, y):
    return float(x) ** float(y)
def radicacion( x, y):
    return math.pow(float(x), float(y))
def logaritmo( x, y):
    return math.log(float(x), float(y))


print "respondiendo... servidorT1"

while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc,addr))

sc.close()
s.close()










