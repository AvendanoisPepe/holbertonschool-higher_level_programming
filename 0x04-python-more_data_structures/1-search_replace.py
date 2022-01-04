#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        acumulador = 0
        listita = my_list.copy()

        for iterador in my_list:
            if iterador == search:
                listita[acumulador] = replace
            acumulador = acumulador + 1

        return (listita)
