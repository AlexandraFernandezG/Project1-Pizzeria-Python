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
    total=0

    while(salida!='n'):
        n=n+1
        print('Pizza numero ', n, '\n')
        
        #Solicitud de tamaño
        print('Por favor, seleccione el tamaño de su pizza\n')
        
        tamaño = accion.solicitar_tamaño()
        precio = precio + historial.precioxtamaño(tamaño)

        #Solicitud de ingredientes

        ingredientes = []
        ingredientes= accion.solicitar_ingrediente()
        precio = precio + accion.calcular_precio_ingrediente(ingredientes)
        

        #Solicitud de bebidas
        res = input('\n¿Desea agregar una bebida a su orden? [s/n]: \n')
        if(res=='s'):
            bebidas = accion.solicitar_bebida()
            precio = precio + accion.calcular_precio_bebida(bebidas)
        else:
            bebidas = []
        
        
        #Delivery
        respuestaDelivery = input('\n¿Desea hacer delivery de su orden? [s/n]: \n').lower()

        if (respuestaDelivery == 's'):

            lugar = accion.solicitar_delivery()
            precio += historial.precioDelivery(lugar)
            #Resumen del pedido
            print('Subtotal a pagar por una pizza '+accion.consultar_nombre_tamaño(tamaño)+ ' con '+ accion.consultar_nombre_ingredientes(ingredientes) +' y '+accion.consultar_nombre_bebidas(bebidas)+ ' a '+ accion.consultar_nombre_delivery(lugar) +': '+str(precio))
            total = total+precio
            precio=0 
        else:
            #Resumen del pedido
            print('Subtotal a pagar por una pizza '+accion.consultar_nombre_tamaño(tamaño)+ ' con '+ accion.consultar_nombre_ingredientes(ingredientes) +' y '+accion.consultar_nombre_bebidas(bebidas)+': '+str(precio))
            total = total+precio
            precio=0 

        salida = accion.solicitar_confirmacion()

    #Resumen de la compra completa
    print(f'El pedido tiene un total de {n} pizza(s) por un monto de {total}\n')
    print('¡Gracias por su compra, regrese pronto!\n')

    #Encuesta de satisfaccion
    if (n>0):
        print('\nEn Pizzeria UCAB nos importamos mucho por la opinión de nuestros clientes\n')
        res = input('Le gustaria responder una pregunta de satisfacción con el fin de mejorar nuestra atención y servicios?[s/n]: \n')
        if (res == 's'):
            print('\n¿Cómo evaluaría nuestro servicios en escala del 1 al 3? (siendo el 3 como excelente):')
            accion.respuesta_puntuacion()
        else:
            print('Que tenga un buen día')
            print('***************************************************************************************')
        
inicio()


#if (__name__ == "__main__"):
#   import sys
#   inicio()