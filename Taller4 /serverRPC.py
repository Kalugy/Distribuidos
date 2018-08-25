from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import math
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8008),
                            requestHandler=RequestHandler)
server.register_introspection_functions()



# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'div').
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

server.register_instance(MyFuncs())

# Run the server's main loop
server.serve_forever()
