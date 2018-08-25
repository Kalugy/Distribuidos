import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:9514    ')


print 'Operaciones: \n - suma o "+" \n - resta o "-" \n - multiplicar o "*" \n - dividir o "/'
print ' - potencia o "^" \n - logaritmo \n - radicacion'
num=raw_input("Ingrese la siguiente sintaxis: numero1 operacion numero2: ")



palabra1=""
palabra2=""
palabra3=""
cuenta=0
contador=0
#cuando cuantas veces esta un signo dentro de la palabra y las separa segun la cantidad de signos
for carac in num:
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
    puerto1= s.ssuma()
    servidor = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
    print servidor.suma(palabra1,palabra3)

elif(palabra2 == 'resta' or palabra2 == '-'):
    puerto1= s.sresta()
    servidor = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
    print servidor.resta(palabra1,palabra3)
elif(palabra2 == 'multiplicar' or palabra2 == '*'):
    puerto1= s.smultiplicar()
    servidor = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
    print servidor.multiplicar(palabra1,palabra3)
elif(palabra2 == 'dividir' or palabra2 == '/'):
    puerto1= s.sdividir()
    servidor = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
    print servidor.dividir(palabra1,palabra3)
elif(palabra2 == 'potencia' or palabra2 == '^'):
    puerto1= s.spotencia()
    servidor = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
    print servidor.potencia(palabra1,palabra3)
elif(palabra2 == 'logaritmo'):
    puerto1= s.slogaritmo()
    servidor = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
    print servidor.logaritmo(palabra1,palabra3)
elif(palabra2 == 'radicacion'):
    puerto1= s.sradicacion()
    servidor = xmlrpclib.ServerProxy('http://localhost: ' + str(puerto1) )
    print servidor.radicacion(palabra1,palabra3)
else:
    print 'No exite la operacion, servidor de la operacion no encontrado, por favor digite nuevamente'

# Print list of available methods
print s.system.listMethods()
