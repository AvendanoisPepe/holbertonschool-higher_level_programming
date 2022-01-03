#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nuevaLista = []
    for iterador in range(len(my_list)):
        if my_list[iterador] % 2 == 0:
            nuevaLista.append(True)
        else:
            nuevaLista.append(False)
    return (nuevaLista)
