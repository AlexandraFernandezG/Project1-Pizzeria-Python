import acciones as accion
import historial_precios as historial
import os

def inicio():
    os.system('cls')
    print('*********************************')
    print('* BIENVENIDO A LA PIZZERIA UCAB *')
    print('*********************************')
    salida = 's'
    n=0
    precio=0

    while(salida!='n'):
        n=n+1
        print('Pizza numero ', n, '\n')
        
        print('Por favor, seleccione el tamaño de su pizza\n')
        tamaño = accion.solicitar_tamaño()
        precio = precio + historial.precioxtamaño(tamaño)

        print(tamaño, precio)

        salida = 'n'


        
inicio()






#if (__name__ == "__main__"):
#   import sys
#   inicio()