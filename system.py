'''
Modulo System
'''

# Importaciones
from deck import *
from players import *
from evaluador import *

# ---------------------
# repartir_cartas()
# ---------------------
def repartir_cartas(
    jugadores: dict[str,list[list[tuple[int,str]],int,bool]], 
    mazo:list[tuple[int,str]],
    descarte: list[tuple[int,str]]
    ):
    ''' 
    Reparte 7 cartas del mazo a cada participante, dando una carta a cada uno
    hasta llegar a las 7 por cada jugador.
    Entra: jugadores, mazo, descarte
    Sale:
    Nota entra descarte ya que si mazo se queda sin cartas acude a el
    '''
    # Itera jugadores
    for cant in range(7):
        for jugador in jugadores:
            if len(mazo) == 0: 
                # Si el Mazo se queda sin cartas generar otro del descarte
                print(
                    "*" * 20 +
                    "\n El mazo quedó sin cartas\n Mezclando y generando mazo del descarte\n" +
                    "*" * 20 
                    ) 
                rearmar_mazo_del_descarte(mazo, descarte)
            
            # Robar carta del mazo
            carta = robar_carta_mazo(mazo)
            
            # Jugador recibe la carta
            # Se agrega a la mano
            jugadores[jugador][0].append(carta)
        
            # Se agrega a libres
            jugadores[jugador][2].append(carta)


def mostrar_encabezado_turno():
    print()
    print('*' * 30)
    print('       SIGUIENTE TURNO')
    print('*' * 30)


# ---------------------
# comienzo_juego () COMIENZO DE PARTIDA!!!!
# ---------------------
def comienzo_juego(
    jugadores: dict[int,list[str, int, bool]],
    mazo: list[tuple[int,str]], 
    descarte: list[tuple[int,str]] 
    ):
    
    '''
    Funcion que comienza el Juego Chinchon
    Ingresan: 
        -jugadores, 
        -mazo, 
        -pila_descarte
    
    '''
    
    print("\n************** COMIENZO DE JUEGO **************\n")
    
    mostrar_cartas(jugadores)
    
    print("\nCarta visible en pila de descarte: ",descarte[-1])
    print("Cantidad de cartas en descarte: ", len(descarte))
    
    print("Cantidad de cartas en el mazo: ", len(mazo))
    
    # COMIENZO DE TURNOS
    corte = False
    while not corte:
        for jugador in jugadores:
            # Encabezado
            mostrar_encabezado_turno()
            
            # ANALIZAR CARTAS
            analizar(jugadores[jugador])
            
            datos_jugador = jugadores[jugador]
            mostrar_cartas_mano(jugador, datos_jugador)
            
            pila = input(f'Levantas carta del mazo(M) O del descarte(D)[{descarte[-1]}]?: ')
            
        
