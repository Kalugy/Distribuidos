import socket
import sys

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(('localhost', 9882))

print 'Operaciones: \n - suma o "+" \n - resta o "-" \n - multiplicar o "*" \n - dividir o "/'
print ' - potencia o "^" \n - logaritmo \n - radicacion'

numero1=raw_input("Ingrese la siguiente sintaxis: num1 operacion num2: ")
s.send(numero1)
respuesta=s.recv(1024)
print "La operacion es : ", respuesta

s.close()
