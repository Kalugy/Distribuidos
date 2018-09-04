import socket
import sys
 
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(('localhost', 9882))


data1 = raw_input("mensaje a enviar>> ")
s.send(data1)
data2 = raw_input("mensaje a enviar>> ")
s.send(data2)
print "Selecciona una opcion"
print "\t1 - Suma"
print "\t2 - Resta "
print "\t3 - Division"
print "\t4 - Multiplicacion"
print "\t5 - Potencia"
print "\t6 - Radicacion"
print "\t9 - salir"
opcionMenu = raw_input("inserta un numero valor >> ")
s.send(opcionMenu)


recibido = s.recv(1024)
print "---------------------------------"
print "suma recibida servidor = " ,recibido
print "---------------------------------"


s.close()
