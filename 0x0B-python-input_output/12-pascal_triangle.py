#!/usr/bin/python3
"""Modulo pascal_triangle que retorna
una lista de enteros con forma de triangulo
de pascal"""


def pascal_triangle(n):
    """Devuelve el triángulo pascal de n."""
    pt = []
    if n <= 0:
        return pt
    for iterador in range(n):
        pl = []
        pl.append(1)
        if iterador == 0:
            pt.append(pl)
            continue
        for iter in range(1, iterador):
            try:
                pl.append(pt[iterador - 1][iter - 1] + pt[iterador - 1][iter])
            except Exception:
                continue
        pl.append(1)
        pt.append(pl)

    return pt
