#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento de la clase cliente
from pruebas import pruebas_codigo_estudiante
from cliente import cliente
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL


def organizePaymentQueue(queue):
    paydesk = []
    for x in queue:
        client = x
        if client.transaccion == "retirar" or client.transaccion == "consignar":
            paydesk.append(client.nombre)
    return paydesk
    
def organizeInformationQueue(queue):
    info = []
    for x in queue:
        client = x
        if client.transaccion == "ninguna":
            info.append(client.nombre)
    return info

def calculateWithdrawal(queue):
    withdrawalAmount = 0
    for x in queue:
        client = x
        if client.transaccion == "retirar":
            withdrawalAmount += client.cantidad_retirar
    return withdrawalAmount 

def calculateConsignations(queue):
    consignationsAmount = 0
    for x in queue:
        client = x
        if client.transaccion == "consignar":
            consignationsAmount += client.cantidad_consignar
    return consignationsAmount
    
def youngestWithdrawal(queue):
    youngest = 100
    for x in queue:
        client = x
        if client.transaccion == "retirar":
            if client.edad < youngest:
                youngest = client.edad
    if youngest == 100:
        youngest = -1
    return youngest

def youngestInformation(queue):
    youngest = 100
    for x in queue:
        client = x
        if client.transaccion == "ninguna":
            if client.edad < youngest:
                youngest = client.edad
    if youngest == 100:
        youngest = -1
    return youngest

def youngestConsignation(queue):
    youngest = 100
    for x in queue:
        client = x
        if client.transaccion == "consignar":
            if client.edad < youngest:
                youngest = client.edad
    if youngest == 100:
        youngest = -1
    return youngest



"""Fin espacio para programar funciones propias"""

def sede_bancaria(cola_general):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    cola_caja = organizePaymentQueue(cola_general)
    cola_info = organizeInformationQueue(cola_general)
    suma_retiros = calculateWithdrawal(cola_general)
    suma_consignaciones = calculateConsignations(cola_general)
    edad_minima_retiro = youngestWithdrawal(cola_general)
    edad_minima_info = youngestInformation(cola_general)
    edad_minima_consignacion = youngestConsignation(cola_general)
    return cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion

"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
pruebas_codigo_estudiante(sede_bancaria)