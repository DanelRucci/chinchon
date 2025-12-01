'''
Modulo System
'''

# Importaciones
import os

from deck import *
from players import *
from evaluador import *

def borrar_pantalla():
    """
    Borra la consola detectando el sistema operativo.
    """
    # Windows usa el comando 'cls'
    if os.name == 'nt':
        os.system('cls')
    # Linux y macOS (y otros sistemas basados en Unix) usan 'clear'
    else:
        os.system('clear')

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

# ---------------------
# mostrar Encabezado
# ---------------------
def mostrar_encabezado_turno(jugador):
    '''
    Funcion que muestra encabezado del turno con numbre del jugador
    '''
    print()
    print('*' * 41)
    print(f'       SIGUIENTE TURNO - {jugador}')
    print('*' * 41)

# ---------------------
# chequear_puntos()
# ---------------------
def chequear_puntos(nombre, datos_jugador):
    '''
    Funcion que chequea si el jugador se paso del limite de puntos para seguir jugando. Si asi fuera cambia la condicion del jugador (jugador[4]) a False
    Entra: nombre del jugador, datos del jugador
    '''
    if datos_jugador[3] > 100:

        # Marcar la condicion del jugador como False para darlo de baja
        datos_jugador[4] = False

        print(f"\n********** ATENCION **********\nEl jugador {nombre} quedo ELIMINADO!!!!!")
        
# ---------------------
# mostrar_tabla_puntos(jugadores)
# ---------------------
def mostrar_tabla_puntos(jugadores):
    '''
    Muestra informacion de la tabla de puntos
    '''
    print()
    print('*' * 41)
    print(f'************ TABLA DE PUNTOS ************')
    
    for jugador in jugadores:
        print(f". {jugador}      {jugadores[jugador][3]} puntos - condicion en el juego: {jugadores[jugador][4]}")
        
# ---------------------
# contar_jugadores_ok(jugadores)
# ---------------------        
def contar_jugadores_ok(jugadores) -> list[str]:
    '''
    Devuelve lista de jugadores que pueden seguir jugando por su condicion True(puntos < 101)
    Entra: jugadores
    '''
    jugadores_ok = []
    return [jugadores_ok.append(jugador) for jugador in jugadores if jugadores[jugador][4]]
    

     
# ---------------------
# cortar()
# ---------------------
def cortar(nombre, jugadores) -> int:
    '''
    Funcion que inicia proceso de corte
        . suma puntos de cada jugador
        . chequea puntos de cada jugador para marcar la condicion del mismo (sigue participando: True o Perdió: False)
        . devuelve la cantidad de jugadores True
    Entra: nombre del jugador que corta y jugadores(dict)
    Sale: devuelve la cantidad de jugadores True
    '''
    print(f"\n***** Iniciando Proceso de Corte de {nombre} *****\n")
    
    # Contar puntos de cada uno y cargarlo en sus puntajes
    for jugador in jugadores:

        # Sumar puntos
        jugadores[jugador][3] += contar_puntos(jugadores[jugador][2])
        
        # Chequear puntos
        chequear_puntos(jugador, jugadores[jugador])
        
    # Mostrar Tabla de pntos
    mostrar_tabla_puntos(jugadores)
    


            
     
# ---------------------
# barajar_y_dar() -> mazo,
# ---------------------
def barajar_y_dar(jugadores) -> tuple[
    dict[int,list[str, int, bool]],
    list[tuple[int,str]], 
    list[tuple[int,str]] 
    ]:
    '''
    Funcion que:
        . Crea un mazo
        . Mezcla
        . Reparte cartas a jugadores
        . inicia descarte
        
     Devuelve una tupla con datos
    - el mazo (lista de tuplas)
    - la pila de descarte
    '''
    
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
    
    return [mazo,descarte]


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
        -descarte
    
    '''
    
    print("\n***********************************************")
    print("************** COMIENZO DE JUEGO **************")
    print("***********************************************\n")
    
    
    # COMIENZO DE RONDAS
    while sum(1 for jugador in jugadores if jugadores[jugador][4]) > 1: # Repite ciclo de Rondas hasta que quede 1 jugador
        
        print("\n************** COMIENZO DE RONDA **************\n")
        mostrar_cartas(jugadores)
        
        print("\nCarta visible en pila de descarte: ",descarte[-1])
        print("Cantidad de cartas en descarte: ", len(descarte))
        
        print("Cantidad de cartas en el mazo: ", len(mazo))
    
        # COMIENZO DE TURNOS
        corte = False
        while not corte:
            for jugador in jugadores:
                # Encabezado
                mostrar_encabezado_turno(jugador)
                
                # ANALIZAR CARTAS
                analizar(jugador = jugadores[jugador])
                
                datos_jugador = jugadores[jugador]
                mostrar_cartas_mano(jugador, datos_jugador)
                
                # Levantar carta
                while True:
                    carta = levantar_carta(mazo, descarte)
                    # Chequear carta
                    if carta == None:
                        rearmar_mazo_del_descarte(mazo, descarte)
                        continue
                    
                    # Tengo carta levantada
                    print(f"\n  .Carta levantada: {carta}\n")
                    break  
                
                recibir_carta(datos_jugador, carta)
                
                # ANALIZAR CARTAS
                analizar(jugador = datos_jugador)
                
                # Mostrar cartas en mano
                mostrar_cartas_mano(jugador, datos_jugador)
                
                # Se puede cortar ???
                puede_cortar, carta_corte = analizar_cortar(datos_jugador[2])
                if puede_cortar:
                    
                    # PUEDE CORTAR
                    print(f"\n¡¡¡¡¡¡ {jugador} ya puede cortar !!!!!\n")
                    desicion =  input(f"Quiere cortar(1) o seguir jugando(enter): ")
                    
                    if desicion == "1":
                        
                        # Terminar proceso de DESCARTE con la CARTA_CORTE
                        descartar(carta_corte, descarte, jugador, jugadores)
                        
                        # Iniciar Proceso de Corte      
                        corte = True                  
                        # cortar(jugador, jugadores)
                        break
                
                if not corte:
                    proceso_descartar(jugador, jugadores, descarte)

            if corte:
                cortar(jugador, jugadores)
                
        # Chequear Si alguien gano el juego
        jugadores_ok = contar_jugadores_ok(jugadores)
        if len(jugadores_ok) == 1:
            # Hay Ganador
            print(f"\n************** El ganador es: {jugadores_ok} **************\n")
            
            break
        
        # Quitar Juggadores que perdieron
        # quitar_jugadores(jugadores)
        
        # Pregunta si quiere seguir con la siguiente ronda
        seguir = input("Para seguir con la siguiente ronda pulsar enter(ingresa x para salir): ")
        if seguir.upper() == 'X':
            print("Elegiste salir del juego")
            break
        
        borrar_pantalla()
        
        # PONER EN 0 LAS MANOS DE LOS JUGADORES HABILITADOS PARA SEGUIR Y BORRAR LOS INHABILITADOS
        reiniciar_jugadores(jugadores)    
        
        # Volver a mezclar y dar cartas entre los JUGADORES HABILITADOS
        mazo, descarte = barajar_y_dar(jugadores)
                
    # FIN DEL JUEGO
    print("\n************** FIN DE JUEGO **************\n")
          
            
                
            
        
