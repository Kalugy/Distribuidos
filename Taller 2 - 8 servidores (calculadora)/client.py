import socket
print 'taller 1'
host ='localhost'
puerto=9502
socket1=socket.socket()
socket1.connect((host,puerto))
fin=False
#while(fin):
print 'Operaciones: \n - suma o "+" \n - resta o "-" \n - multiplicar o "*" \n - dividir o "/'
print ' - potencia o "^" \n - logaritmo \n - radicacion'
numero1=raw_input("Ingrese la siguiente sintaxis: num1 operacion num2: ")
socket1.send(numero1)
respuesta=socket1.recv(1024)
print "El resultado es: ", respuesta
tiempo=raw_input("Presione enter para finalizar")
"""if(tiempo=='y'):
        fin=False
    else:
        fin=True"""
socket1.close()
