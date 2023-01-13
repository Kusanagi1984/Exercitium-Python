# ordenadaPila.py
# Reconocimiento de ordenación de pilas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 1-febrero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo de dato de las pilas](https://bit.ly/3GTToyK)
# (cuyo código se encuentra en [PilaConListas.hs](https://bit.ly/3vL41xD))
# definir la función
#    ordenadaPila : (Pila[A]) -> bool
# tal que ordenadaPila(p) se verifica si los elementos de la pila p
# están ordenados en orden creciente. Por ejemplo,
#    >>> ordenadaPila(apila(1, apila(5, apila(6, vacia()))))
#    True
#    >>> ordenadaPila(apila(1, apila(0, apila(6, vacia()))))
#    False
# ---------------------------------------------------------------------

from copy import deepcopy
from typing import TypeVar

from hypothesis import given

from src.TAD.pilaConListas import (Pila, apila, cima, desapila, esVacia,
                                   pilaAleatoria, vacia)

A = TypeVar('A', int, float, str)

# 1ª solución
# ===========

def ordenadaPila1(p: Pila[A]) -> bool:
    if esVacia(p):
        return True
    cp = cima(p)
    dp = desapila(p)
    if esVacia(dp):
        return True
    cdp = cima(dp)
    return cp <= cdp and ordenadaPila1(dp)

# 2ª solución
# ===========

# pilaAlista(p) es la lista formada por los elementos de la
# lista p. Por ejemplo,
#    >>> pilaAlista(apila(5, apila(2, apila(3, vacia()))))
#    [3, 2, 5]
def pilaAlista(p: Pila[A]) -> list[A]:
    if esVacia(p):
        return []
    cp = cima(p)
    dp = desapila(p)
    return pilaAlista(dp) + [cp]

# ordenadalista(xs, ys) se verifica si xs es una ordenadalista de ys. Por
# ejemplo,
#    >>> ordenadalista([3,2], [5,3,2,7])
#    True
#    >>> ordenadalista([3,2], [5,3,7,2])
#    False
def ordenadaLista(xs: list[A]) -> bool:
    return all((x <= y for (x, y) in zip(xs, xs[1:])))

def ordenadaPila2(p: Pila[A]) -> bool:
    return ordenadaLista(list(reversed(pilaAlista(p))))

# 3ª solución
# ===========

def ordenadaPila3Aux(p: Pila[A]) -> bool:
    if p.esVacia():
        return True
    cp = p.cima()
    p.desapila()
    if p.esVacia():
        return True
    return cp <= p.cima() and ordenadaPila3Aux(p)

def ordenadaPila3(p: Pila[A]) -> bool:
    q = deepcopy(p)
    return ordenadaPila3Aux(q)

# 4ª solución
# ===========

def ordenadaPila4Aux(p: Pila[A]) -> bool:
    while not p.esVacia():
        cp = p.cima()
        p.desapila()
        if not p.esVacia() and cp > p.cima():
            return False
    return True

def ordenadaPila4(p: Pila[A]) -> bool:
    q = deepcopy(p)
    return ordenadaPila4Aux(q)

# Comprobación de equivalencia de las definiciones
# ================================================

# La propiedad es
@given(p=pilaAleatoria())
def test_ordenadaPila(p: Pila[int]) -> None:
    r = ordenadaPila1(p)
    assert ordenadaPila2(p) == r
    assert ordenadaPila3(p) == r
    assert ordenadaPila4(p) == r

# La comprobación es
#    src> poetry run pytest -q ordenadaPila.py
#    1 passed in 0.31s
