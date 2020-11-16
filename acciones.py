

def solicitar_tamaño():
    print('Opciones:')
    tamaño = input('Tamaños: Familiar ( f ) Grande ( g ) Mediana ( m ) Personal ( p ): ')
    while tamaño not in'fgmpFGMP':
        print('¡Debe seleccionar un tamaño valido!\n')
        tamaño = input('Tamaños: Familiar ( f ) Grande ( g ) Mediana ( m ) Personal ( p ): ')
    return tamaño
    