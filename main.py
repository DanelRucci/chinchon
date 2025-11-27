'''
Modulo inicial
'''
# Importaciones
from  game_init import inicializar
from system import comienzo_juego



jugadores, mazo, descarte = inicializar()

comienzo_juego(jugadores, mazo, descarte)