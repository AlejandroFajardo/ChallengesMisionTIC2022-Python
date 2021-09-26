#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento del módulo csv respectivamente
import csv
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)

def escribir(nombre, delimitador, fila):
    with open(nombre, "w", newline="") as csvfile:
        archivo = csv.writer(csvfile, delimiter=delimitador)
        archivo.writerows(fila)
        
"""Fin espacio para programar funciones propias"""

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    lista = [['Sexo', 'Edad en agnos', 'Concepto']]
    with open("COVCOLI.csv", newline="") as csvfile:
        archivo1 = csv.reader(csvfile, delimiter=",")
        edad_menor = 100
        edad_adultos = []
            
        for i,fila in enumerate(archivo1):
            if i>0:
                lista1 = []
                lista1.append(fila[7])
                edad = int(fila[5])
                
                if int(fila[6]) == 2:
                    edad = edad // 12 
                elif int(fila[6]) == 3:
                    edad = edad // (12*30)
                lista1.append(edad)
                
                if edad < edad_menor:
                    edad_menor = edad 
                    age_youngest = int(fila[5])
                    unit_youngest = int(fila[6])
                
                if edad <= 5:
                    lista1.append("primera infancia")
                elif edad <= 11:
                    lista1.append("infante")
                elif edad <= 17:
                    lista1.append("adolescente")
                elif edad <= 59: 
                    lista1.append("adulto")
                else:
                    lista1.append("persona mayor")
                    
                if edad > 18:
                    if fila[8] == "Fallecido":
                        edad_adultos.append(edad) 
                lista.append(lista1)
                
    escribir("analisis_covcol1.csv", ";", lista)
    
   
    mean_alive_g = 0.0
    
    for edades in edad_adultos:
        mean_alive_g += edades
    mean_alive_g = mean_alive_g/len(edad_adultos) 
    
    print(age_youngest)
    print(unit_youngest)
    print(mean_alive_g)
    return age_youngest, unit_youngest, mean_alive_g

"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
solucion()
#pruebas_codigo_estudiante(solucion)
