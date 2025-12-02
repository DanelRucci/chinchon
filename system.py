from __future__ import annotations
from typing import Dict, List, Tuple, Union, Any
import os
from deck import (
    crear_mazo,
    mezclar_mazo,
    iniciar_descarte,
    robar_carta_mazo,
    rearmar_mazo_del_descarte,
)
from players import (
    mostrar_cartas,
    mostrar_cartas_mano,
    reiniciar_jugadores,
)
from evaluador import (
    contar_puntos,
    analizar,
    levantar_carta,
    recibir_carta,
    analizar_cortar,
    descartar,
    proceso_descartar,
)
Card = Tuple[int, str]
PlayerData = List[Any]  # [mano, juegos, libres, puntos, condicion]
PlayerKey = Union[str, int]
PlayersDict = Dict[PlayerKey, PlayerData]
class System:
    """Clase que agrupa las funciones del módulo System original como métodos OOP."""
    def __init__(self) -> None:
        pass
    def borrar_pantalla(self) -> None:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    def mostrar_encabezado_turno(self, jugador: PlayerKey) -> None:
        print()
        print("*" * 41)
        print(f"       SIGUIENTE TURNO - {jugador}")
        print("*" * 41)
    # Reparto y mazo
    def repartir_cartas(self, jugadores: PlayersDict, mazo: List[Card], descarte: List[Card]) -> None:
        for _round in range(7):
            for nombre, datos in jugadores.items():
                if len(mazo) == 0:
                    print(
                        "*" * 20
                        + "\n El mazo quedó sin cartas\n Mezclando y generando mazo del descarte\n"
                        + "*" * 20
                    )
                    rearmar_mazo_del_descarte(mazo, descarte)
                carta = robar_carta_mazo(mazo)
                datos[0].append(carta)
                datos[2].append(carta)
    def barajar_y_dar(self, jugadores: PlayersDict) -> Tuple[List[Card], List[Card]]:
        mazo: List[Card] = crear_mazo()
        print("- Mazo Iniciado!!!")
        mezclar_mazo(mazo)
        print("- Mazo mezclado!!!")
        # repartir cartas
        self.repartir_cartas(jugadores, mazo, descarte=[])
        # iniciar pila de descarte
        descarte: List[Card] = iniciar_descarte(mazo)
        return mazo, descarte
    def chequear_puntos(self, nombre: PlayerKey, datos_jugador: PlayerData) -> None:
        if datos_jugador[3] > 100:
            datos_jugador[4] = False
            print(f"\n********** ATENCION **********\nEl jugador {nombre} quedo ELIMINADO!!!!!")
    def mostrar_tabla_puntos(self, jugadores: PlayersDict) -> None:
        print()
        print("*" * 41)
        print(f"************ TABLA DE PUNTOS ************")
        for nombre, datos in jugadores.items():
            print(f". {nombre}      {datos[3]} puntos - condicion en el juego: {datos[4]}")
    def contar_jugadores_ok(self, jugadores: PlayersDict) -> List[PlayerKey]:
        return [nombre for nombre, datos in jugadores.items() if datos[4]]
    def cortar(self, nombre: PlayerKey, jugadores: PlayersDict) -> int:
        print(f"\n***** Iniciando Proceso de Corte de {nombre} *****\n")
        for jugador_nombre, datos in jugadores.items():
            puntos_sumados = contar_puntos(datos[2])
            datos[3] += puntos_sumados
            self.chequear_puntos(jugador_nombre, datos)
        self.mostrar_tabla_puntos(jugadores)
        jugadores_ok = self.contar_jugadores_ok(jugadores)
        return len(jugadores_ok)
        ## el flujo del juego
    def comienzo_juego(self, jugadores: PlayersDict, mazo: List[Card], descarte: List[Card]) -> None:
        print("\n***********************************************")
        print("************** COMIENZO DE JUEGO **************")
        print("***********************************************\n")
        chinchon: Dict[str, Union[bool, PlayerKey]] = {}
        chinchon["chinchon"] = [False, ""]
        while sum(1 for jugador in jugadores if jugadores[jugador][4]) > 1 and not chinchon["chinchon"][0]:
            print("\n************** COMIENZO DE RONDA **************\n")
            mostrar_cartas(jugadores)
            print("\nCarta visible en pila de descarte: ", descarte[-1] if descarte else None)
            print("Cantidad de cartas en descarte: ", len(descarte))
            print("Cantidad de cartas en el mazo: ", len(mazo))
            corte = False
            while not corte:
                for jugador in jugadores:
                    self.mostrar_encabezado_turno(jugador)
                    if analizar(jugador=jugadores[jugador]):
                        chinchon["chinchon"] = [True, jugador]
                    datos_jugador = jugadores[jugador]
                    mostrar_cartas_mano(jugador, datos_jugador)
                    while True:
                        carta = levantar_carta(mazo, descarte)
                        if carta is None:
                            rearmar_mazo_del_descarte(mazo, descarte)
                            continue
                        print(f"\n  .Carta levantada: {carta}\n")
                        break
                    recibir_carta(datos_jugador, carta)
                    if analizar(jugador=datos_jugador):
                        chinchon["chinchon"] = [True, jugador]
                    mostrar_cartas_mano(jugador, datos_jugador)
                    puede_cortar, carta_corte = analizar_cortar(datos_jugador[2])
                    if puede_cortar:
                        print(f"\n¡¡¡¡¡¡ {jugador} ya puede cortar !!!!!\n")
                        desicion = input(f"Quiere cortar(1) o seguir jugando(enter): ")
                        if desicion == "1":
                            descartar(carta_corte, descarte, jugador, jugadores)
                            corte = True
                            break
                    if not corte:
                        proceso_descartar(jugador, jugadores, descarte)
                if corte:
                    self.cortar(jugador, jugadores)
            jugadores_ok = self.contar_jugadores_ok(jugadores)
            if len(jugadores_ok) == 1:
                print(f"\n************** El ganador es: {jugadores_ok} **************\n")
                break
            elif chinchon["chinchon"][0]:
                ganador = chinchon["chinchon"][1]
                print(f"\n************** El ganador es: {ganador} **************\n")
                print("HA FORMADO CHINCHON!!!!!!!!!!!!!!!!")
                break
            seguir = input("Para seguir con la siguiente ronda pulsar enter(ingresa x para salir): ")
            if seguir.upper() == "X":
                print("Elegiste salir del juego")
                break
            self.borrar_pantalla()
            reiniciar_jugadores(jugadores)
            mazo, descarte = self.barajar_y_dar(jugadores)
        print("\n************** FIN DE JUEGO **************\n")
_system = System()
def borrar_pantalla() -> None:
    return _system.borrar_pantalla()
def comienzo_juego(jugadores, mazo, descarte) -> None:
    return _system.comienzo_juego(jugadores, mazo, descarte)
def barajar_y_dar(jugadores):
    return _system.barajar_y_dar(jugadores)
