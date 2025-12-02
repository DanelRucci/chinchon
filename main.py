"""Modulo inicial (entrypoint)."""
from __future__ import annotations
from game_init import inicializar
from system import comienzo_juego, borrar_pantalla
class MainApp:
    @staticmethod
    def run() -> None:
        borrar_pantalla()
        print("Bienvenido al juego del CHINCHON\n")
        while True:
            cant = input("Cuantos jugadores quieres crear? (2-3-4): ")
            try:
                cant = int(cant)
                if cant in range(2, 5):
                    break
                else:
                    print("Error: Debes Ingresar un numero entre 2 y 4, luego pulsa enter")
            except ValueError:
                print("Error: Debes Ingresar un numero entre 2 y 4, luego pulsa enter")
        jugadores, mazo, descarte = inicializar(cant)
        comienzo_juego(jugadores, mazo, descarte)
## lo tengo en vs
##if __name__ == "__main__":
    MainApp.run()
