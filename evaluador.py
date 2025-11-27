'''
Modulo Evaluador
'''

# ---------------------
# reporte()
# ---------------------
def reporte(cartas: list[tuple[int,str]]) -> tuple[
    dict[int,int],
    dict[str,int]
]:
    '''
    Funcion reporte() recibe de 3 a 7 tuplas(cartas) y devuelve 2 diccionarios
    .- repeticiones: clave: numero, valor: cantidad de repeticiones
    .- palos
    '''
    
    if len(cartas) < 3 or len(cartas) > 8:
        return None
    
    repeticiones = {}
    palos = {}
    
    for carta in cartas:
        # Evaluar REPETICIONES
        numero = carta[0]
        if numero in repeticiones:
            repeticiones[numero] +=1
        else:
            repeticiones[numero] =1
        
        # Evaluar PALOS
        palo = carta[1]
        if palo in palos:
            palos[palo].append(carta[0]) 
        else:
            palos[palo] = [carta[0]]
    
        
    
    return (repeticiones,palos)

# ---------------------
# hay_escalera()
# ---------------------
def hay_escalera(palos: dict[str,list[int]]) -> bool:
    """'''
    Funcion que comprueba si hay escalera.
    Recibe una lista de tuplas de entero, string
    - las agrupa en el diccionario cartas_por_palo SEGUN PALO
    - devuelve True si hay 3 o mas valores consecutivos de un mismo palo sino devuelve False
    - tambien devuelve False si son menos de 3 tuplas, si son mas de 7 tuplas o si la lista está vacía

    '''"""
    es_escalera = False
    escaleras: dict[str,list[int]] = {} # Registra todas las escaleras que haya. Clave: palo, valor: lista de numeros que forman escalera
    
    # Recorre las listas de numeros por palo
    for palo, numeros in palos.items():
        
        # Inicia Busqueda en un palo
        lista_de_numeros = sorted(numeros)
        escalera_x_palo = 0
        if len(lista_de_numeros) < 3:
            continue

        temp = [lista_de_numeros[0]] # Acumula numeros consecutivos
        for i in range(1, len(lista_de_numeros)):
            
            # El numero actual es consecutivo al anterior???
            if lista_de_numeros[i] == lista_de_numeros[i - 1] + 1:
                temp.append(lista_de_numeros[i]) # Sumarlo a lista temp
                
                # Temp tiene 3 o + elementos?
                if len(temp) >= 3: 
                    
                    # Ya Hay una escalera con el mismo palo???
                    if escalera_x_palo:
                        mismo_palo = palo + '1' # Concatena "palo1"
                        escaleras[mismo_palo] = temp # Guarda SEGUNDA escalera
                    else:
                        escaleras[palo] = temp # Guardar PRIMER escalera
                        
                    escalera_x_palo += 1  # Sumar contador de escalera * palo
                    es_escalera = True # levantar bandera es_escalera
                    
            else:
                temp = [lista_de_numeros[i]]
        
        # Pasar diccionario escaleras a una lista de cartas
        # cartas_escalera = []
        # for palo, numeros in escaleras.items:
        #     juego = []
        #     for numero in numeros:
        #         carta = (numero,palo)
        #         juego.append(carta) # Agrega carta a lista juego
            
        #     # Agrega lista juego a cartas escalera
        #     cartas_escalera.append(juego)

    return es_escalera, escaleras # El diccionario escaleras contiene las cartas de todas las escaleras que hay en lista


# ---------------------
# analizar()
# ---------------------
def analizar(jugador: list[list[tuple[int,str]], list[tuple[int,str]], list[tuple[int,str]],int,bool]):
    '''
    Funcion que envia  las cartas a reporte() para luego evaluar resultados
    
    '''

    cartas = jugador[0]
    libres = jugador[2].copy()
    # libres.extend(cartas)
    
    # Hacer reporte
    repeticiones, palos = reporte(cartas)
    
    # ANALIZAR PIERNAS CON repeticiones
    for repeticion in repeticiones:
        
        # Si el numero "repeticion" se repite 3 o mas veces Buscar las cartas y sumarlas a juego para luego sumarlas a juegos
        if repeticiones[repeticion] >= 3:
            # Recorrer mano y sumar todas las cartas de valor 3 a una juego
            juego = []
            
            pierna = [carta for carta in jugador[0] if carta[0] == repeticion]
            
            for carta in pierna:
                # if carta[0] == repeticion:
                #     juego.append(carta)
                # else:
                #     jugador[2].append(carta) # Si no es la carta de la pierna la Agrega a cartas libres (jugador[2])
                                    
                # Agrega la carta a juego
                juego.append(carta) 
                
                # Borra la carta de la pila de "libres" 
                try:
                    libres.remove(carta)
                except ValueError:
                    pass
                
            jugador[1].append(juego)

            
    
    # ANALIZAR ESCALERAS con palos
    escalera, cartas_escalera = hay_escalera(palos)
    
    if escalera:
        print(f"Cartas_escalera: {cartas_escalera}")
        # Sacando Cartas escaleras de cartas libres
        for palo in cartas_escalera:
            juego = []
            for numero in cartas_escalera[palo]:
                
                # Eliminando el 1 si es del mismo palo que anterior
                if palo[-1:] == "1":
                    palo = palo[:-1]
                    
                carta = (numero, palo)

                # # Saca de libres la carta que forma escalera
                try:
                    libres.remove(carta) 
                except ValueError:
                    pass
                
                # Agregar carta al juego para luego sumarlo a posibles juegos
                juego.append(carta)
                
            # Agregar Cartas escalera a posibles juegos (jugador[1])
            jugador[1].append(juego)
            
    jugador[2] = libres.copy()
    
                
    return jugador