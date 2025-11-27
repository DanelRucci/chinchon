
from game_init import inicializar
from system import *
from evaluador import *

jugadores, mazo, descarte = inicializar()



# 1 pierna de unos + 1 escalera de basto (7,8,9). Libre 11 de espadas
# jugadores["Jugador_1"] = [[(7, 'basto'), (1, 'copa'), (1, 'oro'), (8, 'basto'), (9, 'basto'), (1, 'espada'), (11, 'espada')], [], [(7, 'basto'), (1, 'copa'), (1, 'oro'), (8, 'basto'), (9, 'basto'), (1, 'espada'), (11, 'espada')], 0, True] 

# 1 escalera de copas(1,2,3) + 1 escalera de basto (7,8,9). Libre 11 de espadas
# jugadores["Jugador_1"] = [[(7, 'basto'), (1, 'copa'), (2, 'copa'), (8, 'basto'), (9, 'basto'), (3, 'copa'), (11, 'espada')], [], [(7, 'basto'), (1, 'copa'), (2, 'copa'), (8, 'basto'), (9, 'basto'), (3, 'copa'), (11, 'espada')], 0, True]

# 2 escalera de basto(1,2,3) y (7,8,9). Libre 11 de espadas
jugadores["Jugador_1"] = [[(7, 'basto'), (1, 'basto'), (2, 'basto'), (8, 'basto'), (9, 'basto'), (3, 'basto'), (11, 'espada')], [], [(7, 'basto'), (1, 'basto'), (2, 'basto'), (8, 'basto'), (9, 'basto'), (3, 'basto'), (11, 'espada')], 0, True]

# ANALIZAR CARTAS
jugadores["Jugador_1"] = analizar(jugador = jugadores["Jugador_1"])

datos_jugador = jugadores["Jugador_1"]

mostrar_cartas_mano("Jugador_1", datos_jugador)

# mostrar_cartas_mano("Jugador_1", jugadores["Jugador_1"])
