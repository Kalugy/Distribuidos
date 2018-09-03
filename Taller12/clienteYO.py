from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
import time
import math
import sys

class MyFuncs:
    def suma(self, x, y):
        return float(x) + float(y)
    def resta(self, x, y):
        return float(x) - float(y)
    def multiplicar(self, x, y):
        return float(x) * float(y)
    def dividir(self, x, y):
        return float(x) / float(y)
    def potencia(self, x, y):
        return float(x) ** float(y)
    def radicacion(self, x, y):
        return math.pow(float(x), float(y))
    def logaritmo(self, x, y):
        return math.log(float(x), float(y))

class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):
    def __init__(self):
         threading.Thread.__init__(self)
         self.localServer = SimpleThreadedXMLRPCServer(("localhost",10005))
         
         self.localServer.register_instance(MyFuncs())

    def run(self):
         self.localServer.serve_forever()

server = ServerThread()
server.start() # The server is now running
print "Listo servidor."

class ClientThread(threading.Thread):
    def __init__(self):
		threading.Thread.__init__(self)
		self.s = xmlrpclib.ServerProxy('http://localhost:10006')

    def run(self):
        time.sleep(3)
        print "Llamada cliente"
        self.fin=2
        while(self.fin!=1):
            print 'Operaciones: \n - suma o "+" \n - resta o "-" \n - multiplicar o "*" \n - dividir o "/'
            print ' - potencia o "^" \n - logaritmo \n - radicacion \n - salir '
            self.num=raw_input("Ingrese la siguiente sintaxis: numero1 operacion numero2: ")
            palabra1=""
            palabra2=""
            palabra3=""
            cuenta=0
            contador=0
            #cuando cuantas veces esta un signo dentro de la palabra y las separa segun la cantidad de signos
            for carac in self.num:
                if carac == ' ':
                    cuenta+=1
                else:
                   contador+=1
                   if cuenta==0:
                       palabra1+=carac
                   if cuenta==1:
                       palabra2+=carac
                   if cuenta==2:
                       palabra3+=carac


            if(palabra2 == 'suma' or palabra2 == '+'):
                puerto1= self.s.ssuma()
                servidor = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
                print servidor.suma(palabra1,palabra3)

            elif(palabra2 == 'resta' or palabra2 == '-'):

                puerto1= self.s.sresta()
                servidor2 = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
                
                print servidor2.resta(palabra1,palabra3)

            elif(palabra2 == 'multiplicar' or palabra2 == '*'):

                puerto1= self.s.smultiplicar()
                servidor3 = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )

                print servidor3.multiplicar(palabra1,palabra3)

            elif(palabra2 == 'dividir' or palabra2 == '/'):
                puerto1= self.s.sdividir()
                servidor4 = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
                print servidor4.dividir(palabra1,palabra3)

            elif(palabra2 == 'potencia' or palabra2 == '^'):
                puerto1= self.s.spotencia()
                servidor5 = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )

                print servidor5.potencia(palabra1,palabra3)

            elif(palabra2 == 'logaritmo'):
                puerto1= self.s.slogaritmo()
                servidor6 = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
                print servidor6.logaritmo(palabra1,palabra3)

            elif(palabra2 == 'radicacion'):
                puerto1= self.s.sradicacion()
                servidor7 = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
                print servidor7.radicacion(palabra1,palabra3)

            elif(self.num == 'salir') :
                self.fin=1

                print "adios" 
                sys.exit()    
            else:
                print 'No exite la operacion, servidor de la operacion no encontrado, por favor digite nuevamente'

       


client = ClientThread()
client.start() # The server is now running
