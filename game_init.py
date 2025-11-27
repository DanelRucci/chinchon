from players import *
from deck import *
from system import *

def inicializar(cantidad_jugadores: int = 2) -> tuple[
    dict[int,list[str, int, bool]],
    list[tuple[int,str]], 
    list[tuple[int,str]] 
    ]:
    '''
    inicializar() inicializa: Devuelve una tupla con datos
        - Jugadores (diccionario: clave numero_jugador, valor: lista[nombre:str, puntos:int, estado:bool])
        - el mazo (lista de tuplas)
        - la pila de descarte
        
    Recibe la cantidad de jugadores (4 maximo)
    '''
       
    # Crea Jugadores
    jugadores = iniciar_jugadores(cantidad_jugadores)
    print("- jugadores Iniciados!!!")
    
    # Crea Mazo
    mazo = crear_mazo()
    print("- Mazo Iniciado!!!")
    
    # Mezclar Mazo
    mezclar_mazo(mazo)
    print("- Mazo mezclado!!!")
    
    # Repartir cartas (LO HACE system.repartir_cartas())
    repartir_cartas(jugadores,mazo, descarte=[])
    
    # Iniciar descarte
    descarte = iniciar_descarte(mazo)
    
    return (jugadores, mazo, descarte)
    