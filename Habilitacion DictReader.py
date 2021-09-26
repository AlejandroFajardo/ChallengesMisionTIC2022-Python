# NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento del módulo csv respectivamente
#from pruebas import pruebas_codigo_estudiante
import csv
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
# En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)
def write(rows):
    with open("analisis_covcol4.csv", "w", newline='') as csv_file_write:
        fieldname = ["ID de caso", "Municipio", "Concepto"]
        writer = csv.DictWriter(csv_file_write, delimiter = ';', fieldnames = fieldname)
        writer.writeheader()
        writer.writerows(rows)
            
def calculateAge(row):
    aux = float(row['Edad'])
    youngAge = 0.0
    if aux <= 17 and row['Unidad de medida de edad'] == "1" and row['Estado'] == "Fallecido":
        youngAge = aux
    elif  row['Unidad de medida de edad'] == "2" and row['Estado'] == "Fallecido":
        youngAge = aux/12
    elif  row['Unidad de medida de edad'] == "3" and row['Estado'] == "Fallecido":
        youngAge = aux/365
    return youngAge

"""Fin espacio para programar funciones propias"""

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    contagios_ant = 0
    contagios_young = 0
    mean_dead_y = 0.0
    with open("COVCOLIV.csv", newline='') as csv_file:
        table = csv.DictReader(csv_file, delimiter=",")
        #next(table, None)
        counterAnt = 0
        counterYoung = 0
        counterLines = 0
        counterAge = 0.0
        rows = []
        for row in table:
            if row['Sexo'] == 'M' and row['Estado'] == "Fallecido":
                rows.append({'ID de caso' : row['ID de caso'], "Municipio" : row['Nombre municipio'], "Concepto" : "Masculino fallecido"})
            elif row['Sexo'] == 'M' and row['Estado'] != "Fallecido":
                rows.append({"ID de caso" : row['ID de caso'], "Municipio" : row['Nombre municipio'], "Concepto" : "Masculino sobreviviente"})
            elif row['Sexo'] == 'F' and row['Estado'] == "Fallecido":
                rows.append({"ID de caso" : row['ID de caso'], "Municipio" : row['Nombre municipio'], "Concepto" : "Femenino fallecido"})
            elif row['Sexo'] == 'F' and row['Estado'] != "Fallecido":
                rows.append({"ID de caso" : row['ID de caso'], "Municipio" : row['Nombre municipio'], "Concepto" : "Femenino sobreviviente"})
                     
            if row['Nombre departamento'] == "ANTIOQUIA":
                counterAnt += 1
                
            if int(row['Edad']) <= 17 and row['Unidad de medida de edad'] == "1":
                counterYoung += 1
            elif row['Unidad de medida de edad'] != "1":
                counterYoung += 1
                
            #if (int(row['Edad']) <= 17 and row['Unidad de medida de edad'] == "1") or row['Unidad de medida de edad'] != "1":
                #counterYoung += 1
                
            counterAge += calculateAge(row)
            if counterAge > 0:
                counterLines += 1;
        write(rows)
        contagios_ant = counterAnt
        contagios_young = counterYoung
        mean_dead_y = counterAge / counterLines
    print("en antioquia", contagios_ant)
    print("menores de edad", contagios_young)
    print("edad muertos", mean_dead_y)
    return contagios_ant, contagios_young, mean_dead_y


"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
solucion()
# pruebas_codigo_estudiante(solucion)
