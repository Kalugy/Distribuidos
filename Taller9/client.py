import socket
import sys

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(('localhost', 9889))

print 'Operaciones: \n - suma o "+" \n - resta o "-" \n - multiplicar o "*" \n - dividir o "/'
print ' - potencia o "^" \n - logaritmo \n - radicacion'

numero1=raw_input("Ingrese la siguiente sintaxis: num1 operacion num2: ")
s.send(numero1)
respuesta=s.recv(1024)

s1 = socket.socket()
s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s1.connect(('localhost', int(respuesta)))
s1.send(numero1)
respuesta1=s1.recv(1024)

print respuesta1

s.close()
s1.close()
