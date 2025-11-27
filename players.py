
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
        puntos:int, estado:bool]
    '''
    
    jugadores = {}
    
    for numero in range(1, cantidad + 1):
        
        nombre_jugador = f"Jugador_{numero}"
        jugadores[nombre_jugador] = [[],[],[],0,True]
    
    return jugadores

# ---------------------
# recibir_carta()
# ---------------------
def recibir_carta(jugador, carta:list[tuple[int,str]]):
    print(jugador)
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
    
    print(f'Nombre de jugador: {nombre_jugador}\n')
    print(f' . cartas en la mano: {datos_jugador[0]}')
    print(f' . juegos posibles: {datos_jugador[1]}')
    print(f' . cartas libres: {datos_jugador[2]}\n')
    
    
        
# ---------------------
# devolver_cartas()
# ---------------------
def devolver_cartas(mazo, jugadores):
    for jugador in jugadores.values():
        print(len(mazo))
        mazo.extend(jugador[0])
        print(len(mazo))
    
