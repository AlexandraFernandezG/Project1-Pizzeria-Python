#import keyboard as kb
import historial_precios as hp

def consultar_nombre_tamaño(tamaño):
    tamaño_dict = {'f':'Familiar', 'g':'Grande', 'm':'Mediana', 'p':'Personal' }
    return tamaño_dict[tamaño]

def consultar_nombre_bebida(bebida):
    tamaño_dict = {'1':'Refresco 2 litros', '2':'Refresco litro y medio', '3':'Refresco lata', '4':'Agua Mineral' }
    return tamaño_dict[bebida]

def consultar_nombre_delivery(delivery):
    tamaño_dict = {'mon': 'Montalban', 'paz': 'La Paz', 'par': 'El Paraiso', 'ant': 'Antimano'}
    return tamaño_dict[delivery]

def consultar_bebidas():
    tamaño_dict = {'1':'Refresco 2 litros', '2':'Refresco litro y medio', '3':'Refresco lata', '4':'Agua Mineral' }
    return tamaño_dict

def consultar_ingredientes():
    tamaño_dict = {'ja':'Jamón','ch':'Champiñones','pi':'Pimentón','dq':'Doble Queso','ac':'Aceitunas','pp':'Pepperoni','sa':'Salchichón', }
    return tamaño_dict

def consultar_delivery():
    tamaño_dict = {'mon': 'Montalban', 'paz': 'La Paz', 'par': 'El Paraiso', 'ant': 'Antimano'}
    return tamaño_dict

def consultar_nombre_ingrediente(ingrediente):
    tamaño_dict = {'ja':'Jamón','ch':'Champiñones','pi':'Pimentón','dq':'Doble Queso','ac':'Aceitunas','pp':'Pepperoni','sa':'Salchichón', }
    return tamaño_dict [ingrediente]

def consultar_puntuacion ():
    tamaño_dict = {'1':'*', '2':'**', '3':'***'}
    return tamaño_dict

def consultar_respuesta ():
    tamaño_dict = {'1':'Lamentamos mucho el mal servicio ofrecido, para la próxima esperamos hacerlo mejor','2':'Entendemos, es bueno saber que se puede mejorar',
                  '3':'Qué bueno, siempre tratamos de mantener la mejor calidad y servicio'}
    return tamaño_dict

def solicitar_tamaño():
    print('Opciones:')
    tamaño = input('Tamaños: Familiar ( f ) Grande ( g ) Mediana ( m ) Personal ( p ): ')
    while tamaño not in 'fgmp' or tamaño == '':
        print('¡Debe seleccionar un tamaño valido!\n')
        tamaño = input('Tamaños: Familiar ( f ) Grande ( g ) Mediana ( m ) Personal ( p ): ')
    return tamaño

def solicitar_confirmacion():
    salida = input('¿Desea continuar [s/n]?: \n')
    while salida not in 'snSN' or salida == '':
        print('Opcion no valida.\n')
        salida = input('¿Desea continuar [s/n]?: \n')
    return salida

def solicitar_bebida():
    salida,bebidas='s',[]
    print('Bebidas:')
    historial_bebidas = consultar_bebidas()
    for codigo,nombre in historial_bebidas.items():
        print(nombre, '  ', f'({codigo})')
    while(salida=='s'):
        bebida = input('\nIndique bebida: ')
        if bebida not in '1234':
            print('¡Debe seleccionar un codigo de bebida valido!\n')
        elif bebida in '1234': 
            bebidas.append(bebida)
            salida = input('¿Desea agregar otra bebida? [s/n]: ')
    return bebidas

def solicitar_ingrediente ():
    ingredientes = []
    print('Ingredientes:')
    historial_ingredientes = consultar_ingredientes()
    for codigo,nombre in historial_ingredientes.items():
        print(nombre, '  ', f'({codigo})')
    while True:
        ingrediente = input('\nIndique ingrediente (enter para terminar): ')
        if ingrediente == '': 
            break
        if ingrediente in historial_ingredientes:
            ingredientes.append (ingrediente)
        else:
             print('¡Debe seleccionar un codigo de ingrediente valido!\n')
    
    return ingredientes

def solicitar_delivery ():
    lugar = input('Entrega a: Montalban ( mon ) La Paz ( paz ) El Paraiso ( par ) Antimano ( ant ): ')
    while lugar not in['mon', 'paz', 'par', 'ant']:
        print('¡Debe seleccionar un lugar valido!\n')
        lugar = input('Tamaños: Montalban ( mon ) La Paz ( paz ) El Paraiso ( par ) Antimano ( ant ): ')
    return lugar

def respuesta_puntuacion ():
    historial_puntuacion = consultar_puntuacion()
    respuesta = consultar_respuesta ()
    for codigo,nombre in historial_puntuacion.items():
        print(nombre, '  ', f'({codigo})')
    while True:
        puntuacion = input('\nIndique la puntuacion:\n')
        if puntuacion in historial_puntuacion:
         res = respuesta[puntuacion]
         print ('Gracias por su respuesta')
         print(res)
         print('\n*************************FIN**************************************\n')
         break
        else:
         print('¡Debe seleccionar un codigo de puntuacion valido!\n')

def consultar_nombre_bebidas(bebidas):   
    nombre =''
    n=int(len(bebidas))
    if(n==0):
        nombre='sin bebida'
    elif(n==1):
        nombre= nombre + consultar_nombre_bebida(bebidas[0]) 
    else:
        for i in bebidas:
            if(n>1):
                if(i not in nombre):
                    if(n-1==1):
                        nombre= nombre + consultar_nombre_bebida(i)
                    else: 
                        nombre= nombre + consultar_nombre_bebida(i) +', '
                    n=n-1
                    print(1)
                else:
                    n=n-1
            else:
                nombre= nombre+ ' y ' + consultar_nombre_bebida(i)
    return nombre


def consultar_nombre_ingredientes(ingredientes): 
    nombre =''
    n=int(len(ingredientes))
    if(n==0):
        nombre='0 ingredientes adicionales'
    elif(n==1):
        nombre= nombre + consultar_nombre_ingrediente(ingredientes[0]) 
    else:
        for i in ingredientes:
            if(n>1):
                if(i not in nombre):
                    if(n-1==1):
                        nombre= nombre + consultar_nombre_ingrediente(i)
                    else: 
                        nombre= nombre + consultar_nombre_ingrediente(i) +', '
                    n=n-1
                    print(1)
                else:
                    n=n-1
            else:
                nombre= nombre+ ' y ' + consultar_nombre_ingrediente(i) + ','
    return nombre

def calcular_precio_bebida(bebidas):
    suma=0
    for i in bebidas:
        suma = suma + hp.precioxbebida(i)
    return suma

def calcular_precio_ingrediente(ingredientes):
    suma=0
    for i in ingredientes:
        suma = suma + hp.precioxingrediente(i)
    return suma

