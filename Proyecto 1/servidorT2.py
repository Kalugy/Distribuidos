import socket
import sys
import thread
import math
from numpy import *
from numpy import array


puertoSS=8040		

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s1.bind(('', puertoSS))
s1.listen(10)


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

def concatena(num):
	num1=num.split("?")[0]
	palabra2=num.split("?")[1]
	resultado= num1+palabra2
	return resultado


def mayor(num):
	a=num.split("?")[0]
	b=num.split("?")[1]
	c=num.split("?")[2]
	d=num.split("?")[3]
	e=num.split("?")[4]
	if a > b and a > c and a > d and a > e:
		maximo = a
	else:
		if b > a and b > c and b > d and b > e:
			maximo = b
		else:
			if c > a and c > b and c > d and c > e:
				maximo = c
			else:
				if d > a and d > b and d > c and d > e:
					maximo = d
				else:
					maximo = e

	resultado= maximo
	return resultado

def memoriaaa (memoria):
	if memoria < 4000:
		return 0

def procesooo (proceso):
	if proceso < 1700:
		return 0

def connection1(sc1, addr1):
	while True:
		proceso=0
		memoria=0
		num=str(sc1.recv(1024))
		if num == "disponible":
			result=memoriaaa(memoria)
			result2=procesooo(proceso)
			if result==result2:
				result3=0
			sc1.send(str(result3))


		num3=num.split("?")[3]	
		num4=num.split("?")[2]	

		if num3 == "oper":
			print num
			memoria= 200
			proceso = 400
			
			result=calculadora(num)
			sc1.send(str(result))		
			memoria=0
			proceso=0
		elif num4=="conca":
			print num
			result=concatena(num)
			sc1.send(str(result))
		else:
			num6=num.split("?")[5]	
			print num
			result=mayor(num)
			sc1.send(str(result))	





print "respondiendo..."

while 1:

    sc1, addr1 = s1.accept()
    print "recibida conexion de la IP: " + str(addr1[0]) + "puerto: " + str(addr1[1])
    print "\n"
    thread.start_new_thread(connection1,(sc1,addr1))

sc1.close()
s1.close()



"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost',  7000 ))
s.listen(10)


def connection(sc, addr):
	num=str(sc.recv(1024))
	print num
	result=calculadora(num)
	sc.send(str(result))




print "respondiendo... servidorT1"

while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
   
    thread.start_new_thread(connection,(sc,addr))

sc.close()
s.close()

"""




