"""tenemos que poner algo aca"""
from __future__ import annotations
from typing import List, Tuple, Optional
import random
Card = Tuple[int, str]
DeckList = List[Card]
class Deck:
    """Operaciones sobre mazo y descarte."""
    @staticmethod
    def mezclar_mazo(mazo: DeckList) -> None:
        """Mezcla el mazo in-place."""
        random.shuffle(mazo)
    @staticmethod
    def iniciar_descarte(mazo: DeckList) -> DeckList:
        """
        Inicia pila de descarte: quita la última carta del mazo y la devuelve en una lista.
        Modifica `mazo` in-place.
        """
        if not mazo:
            return []
        primer_carta = mazo.pop()
        return [primer_carta]
    @staticmethod
    def robar_carta_mazo(mazo: DeckList) -> Optional[Card]:
        """Saca la última carta del mazo y la devuelve o None si no hay."""
        if not mazo:
            return None
        return mazo.pop()
    @staticmethod
    def robar_carta_descarte(descarte: DeckList) -> Optional[Card]:
        """Saca la última carta del descarte y la devuelve o None si no hay."""
        if not descarte:
            return None
        return descarte.pop()
    @staticmethod
    def rearmar_mazo_del_descarte(mazo: DeckList, descarte: DeckList) -> None:
        """
        Vuelca el descarte en el mazo mezclado (in-place).
        Nota: si el descarte está vacío no hace nada.
        """
        if not descarte:
            return
        random.shuffle(descarte)
        # mover todas las cartas del descarte al mazo
        mazo.extend(descarte)
        descarte.clear()
    @staticmethod
    def crear_mazo() -> DeckList:
        """Crea mazo de cartas españolas (1..12 por cada palo)."""
        palos = ["oro", "espada", "basto", "copa"]
        valores = list(range(1, 13))
        mazo = [(valor, palo) for palo in palos for valor in valores]
        return mazo
    @staticmethod
    def levantar_carta(mazo: DeckList, descarte: DeckList) -> Optional[Card]:
        """
        Interacción con el usuario para levantar carta de M(azo) o D(escarte).
        Mantiene la misma interfaz que el código original.
        """
        print("\nLevantando carta...")
        pila = ""
        while pila == "":
            top_desc = descarte[-1] if descarte else None
            entrada = input(f'Elegir (M)azo | (D)escarte {top_desc}?: ')
            if not entrada:
                print("\nError: No ingresaste nada.\nVolvé a intentar...\n")
                continue
            pila = entrada[0].upper()
            if pila == "M":
                carta = Deck.robar_carta_mazo(mazo)
            elif pila == "D":
                carta = Deck.robar_carta_descarte(descarte)
            else:
                print("\nError: Opción no válida. Volvé a intentar...\n")
                pila = ""
                continue
            return carta
        return None
## importaciones de tipo (necesitabamos eso)
def mezclar_mazo(mazo: DeckList) -> None:
    Deck.mezclar_mazo(mazo)
def iniciar_descarte(mazo: DeckList) -> DeckList:
    return Deck.iniciar_descarte(mazo)
def robar_carta_mazo(mazo: DeckList) -> Optional[Card]:
    return Deck.robar_carta_mazo(mazo)
def robar_carta_descarte(descarte: DeckList) -> Optional[Card]:
    return Deck.robar_carta_descarte(descarte)
def rearmar_mazo_del_descarte(mazo: DeckList, descarte: DeckList) -> None:
    Deck.rearmar_mazo_del_descarte(mazo, descarte)
def crear_mazo() -> DeckList:
    return Deck.crear_mazo()
def levantar_carta(mazo: DeckList, descarte: DeckList):
    return Deck.levantar_carta(mazo, descarte)
