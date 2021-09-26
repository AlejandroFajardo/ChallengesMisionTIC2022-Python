def actualizar_estado_pestana(operaciones_usuario, pagina_default):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    
    pila_atras = []
    pagina_actual = pagina_default
    pila_adelante = []
    
    for i in operaciones_usuario:
        if i != "atras" and i != pagina_actual:
            pila_atras.append(pagina_actual)
            pagina_actual = i
            pila_adelante.clear()
        elif i == "atras":
            pila_adelante.append(pagina_actual)
            pagina_actual = pila_atras.pop()
        elif i == "adelante":
            pila_atras.append(pagina_actual)
            pagina_actual = pila_adelante.pop()
    
    print(pila_atras)
    print(pagina_actual)
    print(pila_adelante)
    return pila_atras, pagina_actual, pila_adelante

funciones = ['udea', 'face', 'face', 'atras', 'atras', 'adelante', 'face', 'face']

actualizar_estado_pestana(funciones, 'google')