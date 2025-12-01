
# ---------------------
# iniciar_jugadores()
# ---------------------
def iniciar_jugadores(cantidad: int) -> dict[str,list[list[tuple[int,str]], list[tuple[int,str]], list[tuple[int,str]],int,bool]]:
    '''
    inicializa un Diccionario del formato:
    clave: nombre_de_jugador: str
    valor: list[
        mano:list[tuple[int,str]], 
        juegos:list[tuple[int,str], 
        libres:list[tuple[int,str], 
        puntos:int, 
        estado:bool]
    '''
    
    jugadores = {}
    
    for numero in range(1, cantidad + 1):
        
        nombre_jugador = f"Jugador_{numero}"
        jugadores[nombre_jugador] = [[],[],[],0,True]
    
    return jugadores

# ---------------------
# recibir_carta()
# ---------------------
def recibir_carta(jugador, carta:tuple[int,str]):
    jugador[0].append(carta)
    
# ---------------------
# mostrar_cartas()
# ---------------------
def mostrar_cartas(jugadores: dict[str,list[list[tuple[int,str]],int,bool]]):
    '''
    Funcion muestra las cartas de los jugadores
    ingresa jugadores
    '''
    print("Lista de jugadores y sus cartas *****")
    print("Jugador      Cartas")
    for jugador in jugadores:
        print(jugador, jugadores[jugador][0])

# ---------------------
# mostrar_cartas_mano()
# ---------------------
def mostrar_cartas_mano(nombre_jugador:str, datos_jugador: list[list[tuple[int,str]], list[tuple[int,str]], list[tuple[int,str]],int,bool]):
    '''
    Funcion que muestra las cartas de la mano de Turno
    Muestra:    . las cartas totales
                . debajo los juegos armados 
                . debajo las cartas libres
    entra:  . Nombre del jugador
            . Datos del jugador
    '''
    
    print(f' . cartas en la mano: {datos_jugador[0]}')
    print(f' . juegos posibles: {datos_jugador[1]}')
    print(f' . cartas libres: {datos_jugador[2]}')
    print(f' . puntos en mano: {contar_puntos(datos_jugador[2])}')
    
    
        
# ---------------------
# reiniciar_jugadores()
# ---------------------
def reiniciar_jugadores(jugadores):
    '''
    Funcion que reinicia jugadores:
        . pone en 0 la listas de mano, posibles juegos y libbres
        . borra jugadores que perdierion (condicion False)
    '''
    for jugador in list(jugadores.keys()):
        if jugadores[jugador][4]: # SI el jugador está habilitado para seguir jugando
            jugadores[jugador][0] = []
            jugadores[jugador][1] = []
            jugadores[jugador][2] = []
        else:
            # Si no está habilitado borrarlo
            jugadores.pop(jugador)
    

# ---------------------
# contar_puntos()
# ---------------------
def contar_puntos(cartas: list[tuple[int,str]]):
    '''
    Funcion que cuenta los numeros de las cartas libres del jugador.
    Entra: libres (jugador[2])
    Sale: la cantidad de puntos
    '''
    return sum(carta[0] for carta in cartas)


    
# ---------------------
# descartar()
# ---------------------
def proceso_descartar(jugador: str, jugadores, descarte):
    '''
    funcion que permite el descarte de una carta de la mano de la cual se saca. tambien se saca la carta de libres (jugador[2])
    Entra:  . nombre de jugador
            . jugadores(dict)
            . descarte
    Sale: 
    '''
    print("\nProceso descarte...")
    elegida = ''
    # recorrer cartas
    for carta in jugadores[jugador][0]:
        print(f"{jugadores[jugador][0].index(carta)} - {carta}")
        
    while True:
        elegida = input("Tipea el numero de carta que quieres descartar: ")
        
        # Convertir elegida a entero
        try:
            elegida = int(elegida)
            if elegida in range(8): # Si el elegida esta dentro del rango de las cartas sale para seguir el proceso
                break
            else:
                # Si elegida esta fuera del rango vuelve arriba a pedir numero
                print("Error: debes elegir el numero de carta(0 al 7)")
        except ValueError:
            print("Error: La entra no es válida. Intentalo de nuevo.")
        
    carta = jugadores[jugador][0][elegida]
    
    # Tengo la carta a descartar, ahora a sacarla de la mano
    descartar(carta, descarte, jugador, jugadores)
    
def descartar(carta, descarte, jugador, jugadores):
    '''
    descarte es una funcion que cumple el proceso "fisico" de descartar, o sea, 
        . quita la carta del maso
        . agrega la carta a la pila de descarte
    '''
    print(f"\nDescartando {carta}...\n")

    try:
        jugadores[jugador][0].remove(carta) # Borra carta de mano
        jugadores[jugador][2].remove(carta) # Borra carta de libres
        print(f"tu mano queda: {jugadores[jugador][0]}")
    except ValueError:
        pass
    
    # Agregar carta a la pila de descarte
    descarte.append(carta)
    

        
        
            
    
                    




    
