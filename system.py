from typing import Dict, List, Tuple, Union, Any
import os
from deck import * # se asume que exporta: crear_mazo, mezclar_mazo, iniciar_descarte, robar_carta_mazo, rearmar_mazo_del_descarte, ...
from players import * # se asume que exporta: mostrar_cartas, mostrar_cartas_mano, reiniciar_jugadores, ...
from evaluador import * # se asume que exporta: contar_puntos, analizar, levantar_carta, recibir_carta, analizar_cortar, descartar, proceso_descartar
Card = Tuple[int, str]
PlayerData = List[Any]  # [mano, ?, libres, puntos, condicion]
PlayerKey = Union[str, int]
PlayersDict = Dict[PlayerKey, PlayerData]
class System:
    """
    Clase que agrupa las funciones del modulo.
    """
    def __init__(self) -> None:
        pass
    def borrar_pantalla(self) -> None:
        """Borra la consola detectando el sistema operativo."""
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def mostrar_encabezado_turno(self, jugador: PlayerKey) -> None:
        """Muestra encabezado del turno con nombre del jugador"""
        print()
        print('*' * 41)
        print(f'       SIGUIENTE TURNO - {jugador}')
        print('*' * 41)

    # ---------------------
    # Reparto y mazo
    # ---------------------
    def repartir_cartas(self, jugadores: PlayersDict, mazo: List[Card], descarte: List[Card]) -> None:
        """
        Reparte 7 cartas del mazo a cada participante, una a la vez por ronda.
        Si el mazo se queda sin cartas, reconstruye desde el descarte.
        """
        for _round in range(7):
            # iterar sobre pares clave/valor evita accesos repetidos al diccionario
            for nombre, datos in jugadores.items():
                if len(mazo) == 0:
                    print(
                        "*" * 20
                        + "\n El mazo quedó sin cartas\n Mezclando y generando mazo del descarte\n"
                        + "*" * 20
                    )
                    rearmar_mazo_del_descarte(mazo, descarte)

                carta = robar_carta_mazo(mazo)
                # datos[0] = mano, datos[2] = libres (según uso original)
                datos[0].append(carta)
                datos[2].append(carta)

    def barajar_y_dar(self, jugadores: PlayersDict) -> Tuple[List[Card], List[Card]]:
        """
        Crea un mazo, lo mezcla, reparte cartas a jugadores y devuelve (mazo, descarte).
        Mantiene la semántica original.
        """
        mazo: List[Card] = crear_mazo()
        print("- Mazo Iniciado!!!")

        mezclar_mazo(mazo)
        print("- Mazo mezclado!!!")

        # Repartir cartas
        self.repartir_cartas(jugadores, mazo, descarte=[])
        # Iniciar pila de descarte
        descarte: List[Card] = iniciar_descarte(mazo)

        return mazo, descarte

    # ---------------------
    # Puntuación y corte
    # ---------------------
    def chequear_puntos(self, nombre: PlayerKey, datos_jugador: PlayerData) -> None:
        """
        Si el jugador supera 100 puntos, marca su condicion como False y avisa.
        datos_jugador: lista con la estructura original (índice 3 -> puntos, índice 4 -> condicion)
        """
        if datos_jugador[3] > 100:
            datos_jugador[4] = False
            print(f"\n********** ATENCION **********\nEl jugador {nombre} quedo ELIMINADO!!!!!")

    def mostrar_tabla_puntos(self, jugadores: PlayersDict) -> None:
        """Muestra la tabla de puntos de todos los jugadores (puntos y condicion)."""
        print()
        print('*' * 41)
        print(f'************ TABLA DE PUNTOS ************')
        for nombre, datos in jugadores.items():
            print(f". {nombre}      {datos[3]} puntos - condicion en el juego: {datos[4]}")

    def contar_jugadores_ok(self, jugadores: PlayersDict) -> List[PlayerKey]:
        """
        Devuelve la lista de jugadores que siguen en el juego (condicion True).
        """
        return [nombre for nombre, datos in jugadores.items() if datos[4]]

    def cortar(self, nombre: PlayerKey, jugadores: PlayersDict) -> int:
        """
        Inicia proceso de corte:
          - suma puntos de cada jugador (con contar_puntos sobre sus libres)
          - chequea puntos y marca condicion
          - muestra la tabla de puntos
        Devuelve la cantidad de jugadores aún en juego (True).
        """
        print(f"\n***** Iniciando Proceso de Corte de {nombre} *****\n")

        # Iterar sobre jugadores y actualizar puntos
        for jugador_nombre, datos in jugadores.items():
            puntos_sumados = contar_puntos(datos[2])
            datos[3] += puntos_sumados
            self.chequear_puntos(jugador_nombre, datos)

        # Mostrar tabla actualizada
        self.mostrar_tabla_puntos(jugadores)

        # devolver cantidad de jugadores activos
        jugadores_ok = self.contar_jugadores_ok(jugadores)
        return len(jugadores_ok)

    # ---------------------
    # Flujo de juego principal
    # ---------------------
    def comienzo_juego(self, jugadores: PlayersDict, mazo: List[Card], descarte: List[Card]) -> None:
        """
        Comienzo del juego (bucle principal). Conserva la lógica original.
        """
        print("\n***********************************************")
        print("************** COMIENZO DE JUEGO **************")
        print("***********************************************\n")

        chinchon: Dict[str, Union[bool, PlayerKey]] = {}
        chinchon['chinchon'] = [False, '']  # bandera chinchon: [flag, nombre]

        # Rondas hasta que quede 1 jugador o se haga chinchon
        while sum(1 for jugador in jugadores if jugadores[jugador][4]) > 1 and not chinchon['chinchon'][0]:
            print("\n************** COMIENZO DE RONDA **************\n")
            mostrar_cartas(jugadores)

            print("\nCarta visible en pila de descarte: ", descarte[-1] if descarte else None)
            print("Cantidad de cartas en descarte: ", len(descarte))
            print("Cantidad de cartas en el mazo: ", len(mazo))

            # COMIENZO DE TURNOS
            corte = False
            while not corte:
                for jugador in jugadores:
                    # Encabezado
                    self.mostrar_encabezado_turno(jugador)

                    # ANALIZAR CARTAS (puede devolver True para chinchon)
                    if analizar(jugador=jugadores[jugador]):
                        chinchon['chinchon'] = [True, jugador]

                    datos_jugador = jugadores[jugador]
                    mostrar_cartas_mano(jugador, datos_jugador)

                    # Levantar carta (si None -> reconstruir mazo desde descarte y reintentar)
                    while True:
                        carta = levantar_carta(mazo, descarte)
                        if carta is None:
                            rearmar_mazo_del_descarte(mazo, descarte)
                            continue
                        print(f"\n  .Carta levantada: {carta}\n")
                        break

                    recibir_carta(datos_jugador, carta)

                    # Analizar de nuevo por si se formó chinchon
                    if analizar(jugador=datos_jugador):
                        chinchon['chinchon'] = [True, jugador]

                    # Mostrar cartas en mano
                    mostrar_cartas_mano(jugador, datos_jugador)

                    # ¿Se puede cortar?
                    puede_cortar, carta_corte = analizar_cortar(datos_jugador[2])
                    if puede_cortar:
                        print(f"\n¡¡¡¡¡¡ {jugador} ya puede cortar !!!!!\n")
                        desicion = input(f"Quiere cortar(1) o seguir jugando(enter): ")
                        if desicion == "1":
                            # Terminar proceso de DESCARTE con la CARTA_CORTE
                            descartar(carta_corte, descarte, jugador, jugadores)
                            corte = True
                            break

                    if not corte:
                        proceso_descartar(jugador, jugadores, descarte)

                if corte:
                    # Ejecutar corte y actualizar puntuaciones
                    self.cortar(jugador, jugadores)

            # Chequear si hay ganador por quedar 1
            jugadores_ok = self.contar_jugadores_ok(jugadores)
            if len(jugadores_ok) == 1:
                print(f"\n************** El ganador es: {jugadores_ok} **************\n")
                break
            elif chinchon["chinchon"][0]:
                ganador = chinchon["chinchon"][1]
                print(f"\n************** El ganador es: {ganador} **************\n")
                print("HA FORMADO CHINCHON!!!!!!!!!!!!!!!!")
                break

            # Pregunta si quiere seguir con la siguiente ronda
            seguir = input("Para seguir con la siguiente ronda pulsar enter(ingresa x para salir): ")
            if seguir.upper() == 'X':
                print("Elegiste salir del juego")
                break

            # Limpiar pantalla y reiniciar manos de jugadores activos
            self.borrar_pantalla()
            reiniciar_jugadores(jugadores)

            # Volver a mezclar y dar cartas entre los jugadores habilitados
            mazo, descarte = self.barajar_y_dar(jugadores)

        # FIN DEL JUEGO
        print("\n************** FIN DE JUEGO **************\n")
