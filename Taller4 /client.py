import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8008')


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
    print s.suma(palabra1,palabra3)
elif(palabra2 == 'resta' or palabra2 == '-'):
    print s.resta(palabra1,palabra3)

elif(palabra2 == 'multiplicar' or palabra2 == '*'):
    print s.multiplicar(palabra1,palabra3)

elif(palabra2 == 'dividir' or palabra2 == '/'):
    print s.dividir(palabra1,palabra3)

elif(palabra2 == 'potencia' or palabra2 == '^'):
    print s.potencia(palabra1,palabra3)

elif(palabra2 == 'logaritmo'):
    print s.logaritmo(palabra1,palabra3)

elif(palabra2 == 'radicacion'):
    print s.radicacion(palabra1,palabra3)

else:
    print 'No exite la operacion, servidor de la operacion no encontrado, por favor digite nuevamente'


# Print list of available methods
print s.system.listMethods()
