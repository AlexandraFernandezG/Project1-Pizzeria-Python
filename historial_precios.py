
def precioxtamaño(tamaño):
    historial = {'f':630,'p':280, 'm':430, 'g':580 }
    return historial[tamaño]

def precioxingrediente(ingrediente):
    historial = {'ja':40,'ch':35,'pi':30,'dq':40,'ac':57.5,'pp':38.5, 'sa':62.5}
    return historial[ingrediente]

def precioxbebida(bebida):
    historial = {'1':80,'2':100,'3':150,'4':180}
    return historial[bebida]

def precioDelivery(delivery):
    historial = {'mon': 20, 'paz': 30, 'par': 40, 'ant': 25}
    return historial[delivery]