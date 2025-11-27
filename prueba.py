from deck import *
from players import *
from system import *
from evaluador import *

mazo = crear_mazo()

mezclar_mazo(mazo)
# print (f"Mazo: {mazo}\n")


# iniciar jugadores
jugadores = iniciar_jugadores(2)

mazo = crear_mazo()

mezclar_mazo(mazo)
# print (f"Mazo: {mazo}\n")

# repartir_cartas(jugadores,mazo,descarte=[])
# mostrar_cartas(jugadores)

# descarte = iniciar_descarte(mazo)
# print("Descarte: ", descarte)

# print (f"Mazo: {mazo}\n")


# devolver_cartas(mazo, jugadores)
# print("cartas devueltas")

# mostrar_cartas(jugadores)

# EVALUAR
# print()
# print('*' * 30)
# print('       SIGUIENTE TURNO')
# print('*' * 30)

# jugadores["Jugador_1"] = [[(7, 'basto'), (1, 'copa'), (1, 'oro'), (8, 'basto'), (9, 'basto'), (1, 'espada'), (11, 'espada')], [], [], 0, True]
# jugadores["Jugador_1"] = [[(7, 'basto'), (1, 'copa'), (2, 'copa'), (8, 'basto'), (9, 'basto'), (3, 'copa'), (11, 'espada')], [], [], 0, True]
jugadores["Jugador_1"] = [[(7, 'basto'), (1, 'basto'), (2, 'basto'), (8, 'basto'), (9, 'basto'), (3, 'basto'), (11, 'espada')], [], [], 0, True]

# ANALIZAR CARTAS
jugadores["Jugador_1"] = analizar(jugador = jugadores["Jugador_1"])

datos_jugador = jugadores["Jugador_1"]

mostrar_cartas_mano("Jugador_1", datos_jugador)

# mostrar_cartas_mano("Jugador_1", jugadores["Jugador_1"])
