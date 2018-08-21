import socket

print 'Taller 2 - Calculadora 8 servidores'
host ='localhost'
puerto=9509
socket1=socket.socket()
#definimos la conecion por un puerto y un host
socket1.connect((host,puerto))
#mensaje en el cliente
print 'Operaciones: \n - suma o "+" \n - resta o "-" \n - multiplicar o "*" \n - dividir o "/'
print ' - potencia o "^" \n - logaritmo \n - radicacion'
numero1=raw_input("Ingrese la siguiente sintaxis: numero1 operacion numero2: ")
#Recibe el numero y lo envia al socket conectado
socket1.send(numero1)

operhost=socket1.recv(1024)
operpuerto=socket1.recv(1024)

socket2=socket.socket()
socket2.connect((operhost,int(operpuerto)))

socket2.send(numero1)

#recibe el dato que enviar el server
respuesta=socket2.recv(1024)
#muestra el resultado
print "El resultado es: ", respuesta
tiempo=raw_input("Presione enter para finalizar, Adios")
#Cerramos el servidor
socket1.close()
socket2.close()
