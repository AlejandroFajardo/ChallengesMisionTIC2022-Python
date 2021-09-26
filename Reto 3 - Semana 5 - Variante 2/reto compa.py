#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
#from pruebas import pruebas_codigo_estudiante

#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

mensaje_a_traducir = ".... --- .-.. .- / -- ..- -. -.. ---"
mensaje_a_traducir1 = ".... . -- --- ... / . -. -.-. --- -. - .-. .- -.. --- / ..- -. .- / .--. .-.. .- -. - .- / -. ..- -. -.-. .- / .- -. - . ... / ...- .. ... - .-"
mensaje_a_traducir2 = "-. --- ... / .... .- -. / .--. .. -.-. .- -.. --- / -.. --- ... / -- --- ... --.- .. - --- ..."
mensaje_a_traducir3 = "- . -. . -- --- ... / -.-. --- -- .. -.. .- / .--. .- .-. .- / - .-. . ... / -.. .. .- ... / -- .- ..."


def traductor_espanol(mensaje_traducir):
    
    morse = {'/' : ' ', '.-' : 'A', '-...':'B', '-.-.' : 'C', '-..' :'D', '.': 'E', ##Diccionario para comparar las letras en código morse y en el alfabeto español
         '..-' :'F', '--.' : 'G', '....': 'H', '..': 'I', '.---' : 'J', '-.-' : 'K',
         '.-..': 'L', '--' :'M', '-.' : 'N', '---' : 'O', '.--.' : 'P', '--.-' : 'Q',
         '.-.' : 'R', '...' : 'S', '-' : 'T', '..-' : 'U', '...-' : 'V', '.--' : 'W',
         '-..-' : 'X', '-.--' : 'Y', '--..' : 'Z' }
    
    mensaje = mensaje_traducir.split() ##Separar cada letra de la palabra y guardarlo en una lista
    mensaje_traducido = "" ##Inicializamos un contador con una lista vacía, aquí guardaremos nuestro mensaje traducido
    #for i in range(len(mensaje)):
        #mensaje_traducido = mensaje_traducido + morse[mensaje[i]]

    for j in mensaje:
        mensaje_traducido = mensaje_traducido + morse[j]
    
    return mensaje_traducido

mensaje1=traductor_espanol(mensaje_a_traducir)
print(mensaje1,"hola")
"""
Esta línea de código que sigue, permite probar si su ejercicio es correcto
"""
#NO ELIMINAR LA SIGUIENTE LÍNEA DE CÓDIGO
#pruebas_codigo_estudiante(traductor_espanol)