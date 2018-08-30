import socket
print 'taller 1'
host ='localhost'
puerto=9986
socket1=socket.socket()
socket1.connect((host,puerto))
fin=False
#while(fin):
numero1=raw_input("Ingrese la siguiente sintaxis: num1 operacion num2}")
socket1.send(numero1)
respuesta=socket1.recv(1024)
print "La operacion es : ", respuesta
tiempo=raw_input("Desea continuar operando y/f")
"""if(tiempo=='y'):
        fin=False
    else:
        fin=True"""
socket1.close()
