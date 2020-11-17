import keyboard as kb
import historial_precios as hp

def consultar_nombre_tamaño(tamaño):
    tamaño_dict = {'f':'Familiar', 'g':'Grande', 'm':'Mediana', 'p':'Personal' }
    return tamaño_dict[tamaño]

def consultar_nombre_bebida(bebida):
    tamaño_dict = {'1':'Refresco 2 litros', '2':'Refresco litro y medio', '3':'Refresco lata', '4':'Agua Mineral' }
    return tamaño_dict[bebida]

def consultar_bebidas():
    tamaño_dict = {'1':'Refresco 2 litros', '2':'Refresco litro y medio', '3':'Refresco lata', '4':'Agua Mineral' }
    return tamaño_dict

def solicitar_tamaño():
    print('Opciones:')
    tamaño = input('Tamaños: Familiar ( f ) Grande ( g ) Mediana ( m ) Personal ( p ): ')
    while tamaño not in'fgmp':
        print('¡Debe seleccionar un tamaño valido!\n')
        tamaño = input('Tamaños: Familiar ( f ) Grande ( g ) Mediana ( m ) Personal ( p ): ')
    return tamaño

def solicitar_confirmacion():
    salida = input('¿Desea continuar [s/n]?: ')
    while salida not in 'snSN':
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

def consultar_nombre_bebidas(bebidas):   #En proceso
    nombre =''
    n=len(bebidas)
    if(n==0):
        nombre='sin bebida'
    else:
        if(n!=1):
            for i in bebidas:
                if(i not in nombre):
                    nombre= nombre + consultar_nombre_bebida(i) +','
                    n=n-1
                else:
                    n=n-1
        else:
             for i in bebidas:
                nombre= nombre + consultar_nombre_bebida(i) 
    return nombre

def calcular_precio_bebida(bebidas):
    suma=0
    for i in bebidas:
        suma = suma + hp.precioxbebida(i)
    return suma

