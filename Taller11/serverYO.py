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
    def ssuma(self, palabra1, palabra3):
        print palabra1," + " ,palabra3
        servidor = xmlrpclib.ServerProxy('http://localhost:6005 ')
        res = servidor.suma(palabra1,palabra3)
        return res
        
    def sresta(self, palabra1, palabra3):
        print palabra1," - " ,palabra3
        servidor2 = xmlrpclib.ServerProxy('http://localhost:6502 ')
        res = servidor2.resta(palabra1,palabra3)
        return res
        
    def smultiplicar(self, palabra1, palabra3):
        print palabra1," * " ,palabra3
        servidor3 = xmlrpclib.ServerProxy('http://localhost:7000 ')
        res = servidor3.multiplicar(palabra1,palabra3)
        return res
    def sdividir(self, palabra1, palabra3):
        print palabra1," / " ,palabra3
        servidor4 = xmlrpclib.ServerProxy('http://localhost:7500 ')
        res = servidor4.dividir(palabra1,palabra3)
        return res
    def spotencia(self, palabra1, palabra3):
        print palabra1," ** " ,palabra3
        servidor5 = xmlrpclib.ServerProxy('http://localhost:8000 ')
        res = servidor5.potencia(palabra1,palabra3)
        return res
    def slogaritmo(self, palabra1, palabra3):
        print palabra1," log " ,palabra3
        servidor6 = xmlrpclib.ServerProxy('http://localhost:8502 ')
        res = servidor6.logaritmo(palabra1,palabra3)
        return res
    def sradicacion(self, palabra1, palabra3):
        print palabra1," rad " ,palabra3
        servidor7 = xmlrpclib.ServerProxy('http://localhost:9001 ')
        res = servidor7.radicacion(palabra1,palabra3)
        return res

class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass



class ServerThread(threading.Thread):
    def __init__(self):
         threading.Thread.__init__(self)
         self.localServer = SimpleThreadedXMLRPCServer(("localhost",10073))
         
         self.localServer.register_instance(MyFuncs())
         

    def run(self):
         self.localServer.serve_forever()

server = ServerThread()
server.start() # The server is now running
print "Listo servidor."

class ClientThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.s = xmlrpclib.ServerProxy('http://localhost:10072')

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
                print self.s.suma(palabra1,palabra3)
            elif(palabra2 == 'resta' or palabra2 == '-'):
                print self.s.resta(palabra1,palabra3)

            elif(palabra2 == 'multiplicar' or palabra2 == '*'):
                print self.s.multiplicar(palabra1,palabra3)

            elif(palabra2 == 'dividir' or palabra2 == '/'):
                print self.s.dividir(palabra1,palabra3)

            elif(palabra2 == 'potencia' or palabra2 == '^'):
                print self.s.potencia(palabra1,palabra3)

            elif(palabra2 == 'logaritmo'):
                print self.s.logaritmo(palabra1,palabra3)

            elif(palabra2 == 'radicacion'):
                print self.s.radicacion(palabra1,palabra3)

            elif(self.num == 'salir') :
                self.fin=1
                print "adios" 
                sys.exit()      
            else:
                print 'No exite la operacion, servidor de la operacion no encontrado, por favor digite nuevamente'

       


client = ClientThread()
client.start() # The server is now running
