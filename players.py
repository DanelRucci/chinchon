from __future__ import annotations
from typing import Dict, List, Tuple, Any, Optional
Card = Tuple[int, str]
PlayerData = List[Any]
PlayersDict = Dict[str, PlayerData]
class PlayersManager:
    """Gestión de jugadores y utilidades relacionadas."""
    @staticmethod
    def iniciar_jugadores(cantidad: int) -> PlayersDict:
        """Crea diccionario de jugadores con la estructura original."""
        jugadores: PlayersDict = {}
        for numero in range(1, cantidad + 1):
            nombre_jugador = f"Jugador_{numero}"
            jugadores[nombre_jugador] = [[], [], [], 0, True]  # mano, juegos, libres, puntos, estado
        return jugadores
    @staticmethod
    def recibir_carta(jugador: PlayerData, carta: Card) -> None:
        jugador[0].append(carta)
    @staticmethod
    def mostrar_cartas(jugadores: PlayersDict) -> None:
        print("Lista de jugadores y sus cartas *****")
        print("Jugador Cartas")
        for jugador in jugadores:
            print(jugador, jugadores[jugador][0])
    @staticmethod
    def mostrar_cartas_mano(nombre_jugador: str, datos_jugador: PlayerData) -> None:
        from evaluador import contar_puntos  # import local para evitar circularidades
        print(f" . cartas en la mano: {datos_jugador[0]}")
        print(f" . juegos posibles: {datos_jugador[1]}")
        print(f" . cartas libres: {datos_jugador[2]}")
        print(f" . puntos en mano: {contar_puntos(datos_jugador[2])}")
    @staticmethod
    def reiniciar_jugadores(jugadores: PlayersDict) -> None:
        for jugador in list(jugadores.keys()):
            if jugadores[jugador][4]:
                jugadores[jugador][0] = []
                jugadores[jugador][1] = []
                jugadores[jugador][2] = []
            else:
                jugadores.pop(jugador)
    @staticmethod
    def contar_puntos(cartas: List[Card]) -> int:
        return sum(carta[0] for carta in cartas)
    @staticmethod
    def proceso_descartar(jugador: str, jugadores: PlayersDict, descarte: List[Card]) -> None:
        print("\nProceso descarte...")
        for i, carta in enumerate(jugadores[jugador][0]):
            print(f"{i} - {carta}")
        while True:
            elegida = input("Tipea el numero de carta que quieres descartar: ")
            try:
                elegida_i = int(elegida)
                if 0 <= elegida_i < len(jugadores[jugador][0]):
                    break
                else:
                    print("Error: debes elegir el numero de carta válido")
            except ValueError:
                print("Error: La entrada no es válida. Inténtalo de nuevo.")
        carta = jugadores[jugador][0][elegida_i]
        PlayersManager.descartar(carta, descarte, jugador, jugadores)

    @staticmethod
    def descartar(carta: Card, descarte: List[Card], jugador: str, jugadores: PlayersDict) -> None:
        print(f"\nDescartando {carta}...\n")
        try:
            jugadores[jugador][0].remove(carta)
            jugadores[jugador][2].remove(carta)
        except ValueError:
            pass
        descarte.append(carta)
_default_manager = PlayersManager()
def iniciar_jugadores(cantidad: int):
    return _default_manager.iniciar_jugadores(cantidad)
def recibir_carta(jugador, carta):
    return _default_manager.recibir_carta(jugador, carta)
def mostrar_cartas(jugadores):
    return _default_manager.mostrar_cartas(jugadores)
def mostrar_cartas_mano(nombre_jugador, datos_jugador):
    return _default_manager.mostrar_cartas_mano(nombre_jugador, datos_jugador)
def reiniciar_jugadores(jugadores):
    return _default_manager.reiniciar_jugadores(jugadores)
def contar_puntos(cartas):
    return _default_manager.contar_puntos(cartas)
def proceso_descartar(jugador, jugadores, descarte):
    return _default_manager.proceso_descartar(jugador, jugadores, descarte)
def descartar(carta, descarte, jugador, jugadores):
    return _default_manager.descartar(carta, descarte, jugador, jugadores)
