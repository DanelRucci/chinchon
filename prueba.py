
# Importaciones
from  game_init import inicializar
from system import comienzo_juego, borrar_pantalla

borrar_pantalla()

print ("Bienvenido al juego del CHINCHON\n")
while True:
    cant = input("Cuantos jugadores quieres crear? (2-3-4): ")
    
    # 
    try:
        cant = int(cant)
        if cant in range(2,5):
            break
        else:
            print("Error: Debes Ingresar un numero entre 2 y 4, luego pulsa enter")
    except ValueError:
        print("Error: Debes Ingresar un numero entre 2 y 4, luego pulsa enter")

# Inicializar Juego
jugadores, mazo, descarte = inicializar(cant)
    

# 1 pierna de unos + 1 escalera de basto (7,8,9). Libre 11 de espadas
# jugadores["Jugador_1"] = [[(7, 'basto'), (1, 'copa'), (1, 'oro'), (8, 'basto'), (9, 'basto'), (1, 'espada'), (11, 'espada')], [], [(7, 'basto'), (1, 'copa'), (1, 'oro'), (8, 'basto'), (9, 'basto'), (1, 'espada'), (11, 'espada')], 0, True] 

# 1 escalera de copas(1,2,3) + 1 escalera de basto (7,8,9). Libre 11 de espadas
# jugadores["Jugador_1"] = [[(7, 'basto'), (1, 'copa'), (2, 'copa'), (8, 'basto'), (9, 'basto'), (3, 'copa'), (11, 'espada')], [], [(7, 'basto'), (1, 'copa'), (2, 'copa'), (8, 'basto'), (9, 'basto'), (3, 'copa'), (11, 'espada')], 0, True]

# 2 escalera de basto(1,2,3) y (7,8,9). Libre 11 de espadas
#jugadores["Jugador_1"] = [[(1, 'basto'), (2, 'basto'), (3, 'basto'), (4, 'basto'), (7, 'basto'),  (8, 'basto'), (9, 'basto')], [], [], 0, True]
#jugadores["Jugador_2"][3] = 95

# CHINCHON
jugadores["Jugador_1"] = [[(1, 'basto'), (2, 'basto'), (3, 'basto'), (4, 'basto'), (5, 'basto'),  (6, 'basto'), (7, 'basto')], [], [], 0, True]


# ANALIZAR CARTAS
# jugadores["Jugador_1"] = analizar(jugador = jugadores["Jugador_1"])

# datos_jugador = jugadores["Jugador_1"]

# mostrar_cartas_mano("Jugador_1", datos_jugador)

# mostrar_cartas_mano("Jugador_1", jugadores["Jugador_1"])

# COMENZAR JUEGO
comienzo_juego(jugadores, mazo, descarte)
