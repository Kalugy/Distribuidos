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

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


class MyFuncs:
    def ssuma(self):
        return 6006
    def sresta(self):
        return 6500
    def smultiplicar(self):
        return 7000
    def sdividir(self):
        return 7500
    def spotencia(self):
        return 8000
    def slogaritmo(self):
        return 8500
    def sradicacion(self):
        return 9000



class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass



class ServerThread(threading.Thread):
    def __init__(self):
         threading.Thread.__init__(self)
         self.localServer = SimpleThreadedXMLRPCServer(("localhost",10006))
         
         self.localServer.register_instance(MyFuncs())
         

    def run(self):
         self.localServer.serve_forever()

server = ServerThread()
server.start() # The server is now running
print "Listo servidor."

class ClientThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.s = xmlrpclib.ServerProxy('http://localhost:10005')

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
                server = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
                print server.suma(palabra1,palabra3)

            elif(palabra2 == 'resta' or palabra2 == '-'):
                puerto1= self.s.sresta()
                server2 = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
                print server2.resta(palabra1,palabra3)

            elif(palabra2 == 'multiplicar' or palabra2 == '*'):
                puerto1= self.s.smultiplicar()
                server3 = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
                print server3.multiplicar(palabra1,palabra3)

            elif(palabra2 == 'dividir' or palabra2 == '/'):
                puerto1= self.s.sdividir()
                server4 = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
                print server4.dividir(palabra1,palabra3)

            elif(palabra2 == 'potencia' or palabra2 == '^'):
                puerto1= self.s.spotencia()
                server5 = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
                print server5.potencia(palabra1,palabra3)

            elif(palabra2 == 'logaritmo'):
                puerto1= self.s.slogaritmo()
                server6 = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
                print server6.logaritmo(palabra1,palabra3)

            elif(palabra2 == 'radicacion'):
                puerto1= self.s.sradicacion()
                server7 = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
                print server7.radicacion(palabra1,palabra3)

            elif(self.num == 'salir') :
                self.fin=1
                print "adios" 
                sys.exit()      
            else:
                print 'No exite la operacion, servidor de la operacion no encontrado, por favor digite nuevamente'

       


client = ClientThread()
client.start() # The server is now running
