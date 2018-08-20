import socket
print 'taller 1'
host ='localhost'
puerto=9999
socket1=socket.socket()
socket1.connect((host,puerto))
numero1=raw_input("Ingrese numero:")
socket1.send(numero1)
numero2=raw_input("Ingrese otro numero:")
socket1.send(numero2)
suman=socket1.recv(1024)
print "La suma de : ", numero1, " y ", numero2, "es: ", suman
tiempo=raw_input("presione enter para terminar")
socket1.close()