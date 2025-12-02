from __future__ import annotations
from typing import Dict, List, Tuple
from players import iniciar_jugadores
from system import barajar_y_dar
Card = Tuple[int, str]
PlayerDict = Dict[int, List]
class GameInit:
    """Inicialización del juego."""
    @staticmethod
    def inicializar(cantidad_jugadores: int = 2) -> Tuple[dict, List[Card], List[Card]]:
        """
        Inicializa jugadores, mazo y descarte (mantiene la interfaz original).
        """
        jugadores = iniciar_jugadores(cantidad_jugadores)
        print("- jugadores Iniciados!!!")
        mazo, descarte = barajar_y_dar(jugadores)
        return jugadores, mazo, descarte
def inicializar(cantidad_jugadores: int = 2):
    return GameInit.inicializar(cantidad_jugadores)
    
