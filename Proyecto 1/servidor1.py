import socket
import sys
import thread
import math
from numpy import *
from numpy import array


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 9987 ))
s.listen(10)


def connection(sc, addr):
	num=str(sc.recv(1024))
	print num
	sc.send("se conecto")


print "respondiendo..."

while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc,addr))

sc.close()
s.close()