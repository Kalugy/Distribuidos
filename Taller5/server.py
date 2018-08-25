import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import math
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server1 = SimpleXMLRPCServer(("localhost", 9510 	),
                            requestHandler=RequestHandler)
server1.register_introspection_functions()

servidor = xmlrpclib.ServerProxy('http://localhost:6004 ')
servidorresta = xmlrpclib.ServerProxy('http://localhost:6502')
servidor3 = xmlrpclib.ServerProxy('http://localhost:7000')
servidor4 = xmlrpclib.ServerProxy('http://localhost:7500')
servidor5= xmlrpclib.ServerProxy('http://localhost:8000')
servidor6 = xmlrpclib.ServerProxy('http://localhost:8500')
servidor7 = xmlrpclib.ServerProxy('http://localhost:9000')




class MyFuncs:
    def ssuma(self, palabra1, palabra3):
		print palabra1," + " ,palabra3
		res = servidor.suma(palabra1,palabra3)
		return res
    def sresta(self, palabra1, palabra3):
		return servidorresta.resta(palabra1,palabra3)
    def smultiplicar(self, palabra1, palabra3):
		return servidor3.multiplicar(palabra1,palabra3)
    def sdividir(self, palabra1, palabra3):
		return servidor4.dividir(palabra1,palabra3)
    def spotencia(self, palabra1, palabra3):
		return servidor5.potencia(palabra1,palabra3)
    def slogaritmo(self, palabra1, palabra3):
		return servidor6.logaritmo(palabra1,palabra3)
    def sradicacion(self, palabra1, palabra3):
		return servidor7.radicacion(palabra1,palabra3)

server1.register_instance(MyFuncs())
server1.serve_forever()

# Print list of available methods
#print server.system.listMethods()
print server1.system.listMethods()
