# interior_de_una_lista.py
# Interior de una lista
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 22-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    interior : (List[A]) -> List[A]
# tal que interior(xs) es la lista obtenida eliminando los extremos de
# la lista xs. Por ejemplo,
#    interior([2, 5, 3, 7, 3])  ==  [5, 3, 7]
# ---------------------------------------------------------------------

from typing import List, TypeVar
from hypothesis import given, strategies as st

A = TypeVar('A')

# 1ª solución
def interior1(xs):
    # type: (List[A]) -> List[A]
    return xs[1:][:-1]

# 2ª solución
def interior2(xs):
    # type: (List[A]) -> List[A]
    return xs[1:-1]

# La propiedad de equivalencia es
@given(st.lists(st.integers()))
def test_triangular(xs):
    assert interior1(xs) == interior2(xs)

# La comprobación es
#    src> poetry run pytest -q interior_de_una_lista.py
#    1 passed in 0.21s
