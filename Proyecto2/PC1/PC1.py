
"""PC! RPC"""

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import threading
import os
IP = 'localhost'
PUERTO = 7012
Paginas = {"M1.txt": 8}
CapacidadTotal = {"M1.txt": 8}
Disponibilidad = [0, 0]  # Bloqueado = 1, Desbloqueado = 0

#---------------------------Server-------------------------------#
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2', )


server = SimpleXMLRPCServer((IP, PUERTO), requestHandler=RequestHandler)
server.register_introspection_functions()

#---functions---#
class MyFuncs:
    def ActualizarPagina(self, nombre, contenido):
        if nombre in Paginas:
            lineas = len(open(nombre).readlines())
            if lineas > Paginas[nombre]:
                return 0
            else:
                pagina = open(nombre, "w")
                pagina.write(contenido)
                pagina.close()
                Paginas[nombre] -= lineas
                return 1
        else:
            return -1

    def AgregarCopia(self, nombre, capacidadtotal, capacidadparcial):
        Paginas[nombre] = capacidadparcial
        CapacidadTotal[nombre] = capacidadtotal
        return "Copia agregada"

#---mira la pagina disponible---#
    def BuscarPagina(self, nombre):
        if nombre in Paginas:
            Pos = int(nombre[1]) - 1
            print "El nombre es : ", nombre
            return Paginas[nombre], CapacidadTotal[nombre], Disponibilidad[Pos]
        else:
            return -1

    def PedirCopia(self, nombre):
        if nombre in Paginas:
            Pos = int(nombre[1]) - 1
            if Disponibilidad[Pos] == 0:
                capacidad = Paginas[nombre]
                Archivo = open(nombre, "r")
                contenido = Archivo.read()
                Archivo.close()
                return contenido, capacidad, CapacidadTotal[nombre]
            else:
                return "No"
        else:
            return -1

#---functions de bloqueo de funciones para saber cuando esta libre o no ---#
    def Bloqueo(self, nombre):
        Pos = int(nombre[1]) - 1
        Disponibilidad[Pos] = 1
        return 1

    def Desbloqueo(self, nombre):
        Pos = int(nombre[1]) - 1
        Disponibilidad[Pos] = 0
        return 0


server.register_instance(MyFuncs())
server.serve_forever()
