import socket
import sys
import thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 9882))
s.listen(10)

def connection(sc, addr):
	data1 = sc.recv(1024)
	data2 = sc.recv(1024)
	opcionMenu = sc.recv(10)


	print "recibido", data1, data2, opcionMenu
	enviar = 0
	if opcionMenu=="1":
	    enviar= (int(data1)) + (int(data2))
	elif opcionMenu=="2":
	    enviar= (int(data1)) - (int(data2))
	elif opcionMenu=="3":
	    enviar= (int(data1)) / (int(data2))
	elif opcionMenu=="4":
	    enviar=(int(data1)) * (int(data2))
	elif opcionMenu=="5":
	    enviar= pow(float(data1),(float(data2)))
	elif opcionMenu=="6":
	    enviar=math.sqrt(data1)
	elif opcionMenu=="9":
	    enviar= "salir"

	sc.send(str(int(enviar)))

print "respondiendo..."

while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc,addr))
    
sc.close()
s.close()


