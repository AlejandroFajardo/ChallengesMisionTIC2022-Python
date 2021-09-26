#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento del módulo csv respectivamente
#from pruebas import pruebas_codigo_estudiante
import csv

def solucion():
   MSFT = open('MSFT.csv',newline='')
   archivo = open('analisis_archivo.csv', 'w', newline='')
   
   cabecera = ('Fecha', 'Mean-Min-Max','Concepto')
   archivoW = csv.writer(archivo, delimiter='\t')
   archivoW.writerow(cabecera)
   
   reader = csv.DictReader(MSFT, delimiter=',')
   
   valuesL = []
   valuesH = []
   fechas = []
   for row in reader:
       mean = (float(row["High"]) + float(row["Low"])) / 2
       
       if mean < 207:
           concepto= "MUY BAJO"
       elif mean >= 207 and mean < 221:
           concepto= "BAJO"
       elif mean >= 221 and mean < 235:
           concepto= "MEDIO"
       elif mean >= 235 and mean < 249:
           concepto= "ALTO"
       elif mean >= 249:
           concepto= "MUY ALTO"
       fila = (row["Date"],mean, concepto)
       archivoW.writerow(fila)
       
       valuesL.append(float(row["Low"]))
       valuesH.append(float(row["High"]))
       fechas.append(row["Date"])
       
       lowest_value = min(valuesL)
       date_lowest = fechas[valuesL.index(lowest_value)]
       highest_value = max(valuesH)
       date_highest = fechas[valuesH.index(highest_value)]
   print("fecha del menor prom", date_lowest)
   print("promedio menor", lowest_value)
   print("fecha del mayor prom", date_highest)
   print("promedio mayor", highest_value)
   return date_lowest, lowest_value, date_highest, highest_value

print(solucion())
"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
#pruebas_codigo_estudiante(solucion)