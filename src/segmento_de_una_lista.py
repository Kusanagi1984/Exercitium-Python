# segmento_de_una_lista.py
# Segmento de una lista.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    segmento : (int, int, List[A]) -> List[A]
# tal que segmento(m, n, xs) es la lista de los elementos de xs
# comprendidos entre las posiciones m y n. Por ejemplo,
#    segmento(3, 4, [3, 4, 1, 2, 7, 9, 0])  ==  [1, 2]
#    segmento(3, 5, [3, 4, 1, 2, 7, 9, 0])  ==  [1, 2, 7]
#    segmento(5, 3, [3, 4, 1, 2, 7, 9, 0])  ==  []
# ---------------------------------------------------------------------

from typing import List, TypeVar

A = TypeVar('A')


def segmento(m, n, xs):
    # type: (int, int, List[A]) -> List[A]
    ys = xs[:n]
    return ys[m - 1:]
