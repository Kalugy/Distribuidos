import socket

print 'HOLA Yo exito by Nicolas '
host ='localhost'
puerto=9512
socket1=socket.socket()
#definimos la conecion por un puerto y un host
socket1.connect((host,puerto))
#mensaje en el cliente
print 'Bienvenido al comunicador de grupos \n 1. crear grupo \n 2. Asignar grupo \n 3. Mostrar grupo \n 4. Eliminar grupo'
numero1=raw_input("Ingrese numero de 1 a 4: ")
#Recibe el numero y lo envia al socket conectado
dato=str(host) +' '+ str(puerto) +' '+ str(numero1)
socket1.send(dato)
"""
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
"""
socket1.close()