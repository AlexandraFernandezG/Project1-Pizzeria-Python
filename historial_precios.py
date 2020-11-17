
def precioxtamaño(tamaño):
    historial = {'p':6, 'm':10, 'g':15, 'f':18 }
    return historial[tamaño]

def precioxingrediente(ingrediente):
    historial = {'ja':1,'ch':1,'pi':1,'dq':1,'ac':1,'pp':1}
    return historial[ingrediente]

def precioxbebida(bebida):
    historial = {'1':4,'2':3,'3':1.5,'4':1}
    return historial[bebida]