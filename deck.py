'''
# * Modulo Deck
'''

# Importaciones
import random

# ---------------------
# mezclar_mazo()
# ---------------------
def mezclar_mazo(mazo: list[tuple[int, str]]):
    '''
    Mezcla el mazo en su lugar.
    entra: mazo
    '''
    
    random.shuffle(mazo)

# ---------------------
# iniciar_descarte()
# ---------------------
def iniciar_descarte(mazo:list[tuple[int, str]]) -> list[tuple[int, str]]:
    '''
    Inicia pila de descarte
    Ingresa: el mazo
    Sale: pila de descarte
    Nota: el mazo se modifica quitando la ultima carta que va en el descarte
    '''
    primer_carta = mazo.pop()
    return [primer_carta]

# ---------------------
# Robar_carta_mazo()
# ---------------------
def robar_carta_mazo(mazo:list[tuple[int, str]]):
    '''
    Funcion que saca la última carta del mazo
    Entra: el mazo
    Sale: No devuelve nada ya que el mazo se modifica en el mismo lugar
    '''
    carta = mazo.pop()
    return carta if carta else None

# ---------------------
# Robar_carta_descarte()
# ---------------------
def robar_carta_descarte(descarte:list[tuple[int, str]]):
    '''
    Funcion que saca la última carta de la pila de descarte
    Entra: la pila de descarte
    Sale: No devuelve nada ya que el mazo se modifica en el mismo lugar
    '''
    carta = descarte.pop()
    return carta if carta else None

# ---------------------
# rearmar_mazo_del_descarte()
# ---------------------
def rearmar_mazo_del_descarte(mazo: list[tuple[int,str]], descarte: list[tuple[int,str]]):
    '''
    Funcion que recibe las pilas de mazo vacía y descarte, 
    y llena el mazo con el descarte mezclado
    Entra: pila de mazo y la pila de descarte
    Sale: No devuelve nada ya que el mazo y el descarte se modifican en el mismo lugar
    '''
    mazo = random.shuffle(descarte)
    descarte = []
    
# ---------------------
# crear_mazo()
# ---------------------
def crear_mazo() -> list[tuple[int,str]]:
    ''' 
    Crea Mazo de cartas españolas
    Devuelve: 
        - mazo:list[tuple[int,str]]
    '''
    palos = ["oro", "espada", "basto", "copa"]
    valores = list(range(1,13))

    mazo = [(valor,palo) for palo in palos for valor in valores]
    return mazo





