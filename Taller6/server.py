import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import math
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server1 = SimpleXMLRPCServer(("localhost", 9514 	),
                            requestHandler=RequestHandler)
server1.register_introspection_functions()



class MyFuncs:
    def ssuma(self):
		return 6005
    def sresta(self):
		return 6502
    def smultiplicar(self):
		return 7000
    def sdividir(self):
		return 7500
    def spotencia(self):
		return 8000
    def slogaritmo(self):
		return 8500
    def sradicacion(self):
		return 9001

server1.register_instance(MyFuncs())
server1.serve_forever()

# Print list of available methods
#print server.system.listMethods()
print server1.system.listMethods()
