# NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento del módulo csv respectivamente
#from pruebas import pruebas_codigo_estudiante
import csv
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
# En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)
date_lowest_mean = ""
lowest_mean = 0
date_highest_mean = ""
highest_mean = 0

def write(rows):
    with open("analisis_archivo.csv", "w", newline='') as csv_file_write:
        fieldname = ['Fecha', 'Concepto']
        writer = csv.DictWriter(csv_file_write, delimiter = '\t', fieldnames = fieldname)
        writer.writeheader()
        writer.writerows(rows)

def leer():
     with open("analisis_archivo.csv", newline='') as csv_file:
        table = csv.DictReader(csv_file, delimiter=",")
        for row in table:
            print(row)
            
def findLowestMean(dict):
    date = date_lowest_mean
    lowestMean = lowest_mean
    if lowestMean == 0:
        lowestMean = (float(dict[2]) + float(dict[3]))  / 2
        date = dict[0]
    else:
        aux = (float(dict[2]) + float(dict[3]))  / 2
        if lowestMean > aux:
            lowestMean = aux
            date = dict[0]
    return lowestMean, date

def findHighestMean(dict):
    date = date_highest_mean
    highestMean = highest_mean
    if highestMean == 0:
        highestMean = (float(dict[2]) + float(dict[3]))  / 2
        date = dict[0]
    else:
        aux = (float(dict[2]) + float(dict[3]))  / 2
        if highestMean < aux:
            highestMean = aux
            date = dict[0]
    return highestMean, date
    
"""Fin espacio para programar funciones propias"""

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    with open("GOOG.csv", newline='') as csv_file:
        table = csv.reader(csv_file, delimiter=",")
        next(table, None)
        finalLowest = 0
        finalLowestDate = "" 
        finalHighest = 0
        finalHighestDate = ""
        rows = []
        for row in table:
            auxLowest, auxLowestDate = findLowestMean(row)
            auxHighest, auxHighestDate = findHighestMean(row)
            if finalLowest == 0:
                finalLowest = auxLowest
                finalLowestDate = auxLowestDate
            else:
                if finalLowest > auxLowest:
                    finalLowest = auxLowest
                    finalLowestDate = auxLowestDate
            if finalHighest == 0:
                finalHighest = auxHighest
                finalHighestDate = auxHighestDate
            else:
                if finalHighest < auxHighest:
                    finalHighest = auxHighest
                    finalHighestDate = auxHighestDate
            close  = float(row[4])
            if close < 1624:
                rows.append({'Fecha' : row[0], 'Concepto' : "MUY BAJO"})
            elif close >= 1624 and close < 1854:
                rows.append({'Fecha' : row[0], 'Concepto' : "BAJO"})
            elif close >= 1854 and close < 2084:
                rows.append({'Fecha' : row[0], 'Concepto' : "MEDIO"})
            elif close >= 2084 and close < 2314:
                rows.append({'Fecha' : row[0], 'Concepto' : "ALTO"})
            elif close >= 2314:
                rows.append({'Fecha' : row[0], 'Concepto' : "MUY ALTO"})
        write(rows)
        date_lowest_mean = finalLowestDate
        lowest_mean = finalLowest
        date_highest_mean = finalHighestDate
        highest_mean = finalHighest
    print("fecha del menor prom", date_lowest_mean)
    print("promedio menor", lowest_mean)
    print("fecha del mayor prom", date_highest_mean)
    print("promedio mayor", highest_mean)
    return date_lowest_mean, lowest_mean, date_highest_mean, highest_mean


"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
solucion()
#leer()
# pruebas_codigo_estudiante(solucion)
