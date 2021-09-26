#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
from pruebas import pruebas_codigo_estudiante

#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""



#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES 
morse = {".-" : "A", "-...":"B", "-.-.": "C", "-..":"D","." : "E", "..-." : "F", "--." : "G", "...." :"H", ".." : "I",
        ".---" : "J", "-.-" : "K", ".-.." : "L", "--" : "M", "-." : "N", "---" : "O", ".--." : "P", "--.-" : "Q",
        ".-." : "R", "..." : "S", "-" : "T", "..-" : "U", "...-" : "V", ".--" : "W", "-..-" : "X", "-.--" : "Y", "--.." : "Z",}

def translateLetter(letter):
    if letter in morse:
        return morse[letter]
    else:
        return ""

def translateText(message):
    traduction = ""
    x = message.split(" / ")
    last = len(x)
    for i in range(last):
        morse_word = x[i]
        for morse_letter in morse_word.split():
            letter = translateLetter(morse_letter)
            traduction += letter
        if i != last-1:
            traduction += " "
    return traduction
"""Fin espacio para programar funciones propias"""

def traductor_a_espanol(mensaje_a_traducir):
    #PROGRAMA ACÁ TU SOLUCIÓN
    mensaje_traducido = translateText(mensaje_a_traducir)
    
    return mensaje_traducido

"""
Esta línea de código que sigue, permite probar si su ejercicio es correcto
"""
#NO ELIMINAR LA SIGUIENTE LÍNEA DE CÓDIGO
pruebas_codigo_estudiante(traductor_a_espanol)