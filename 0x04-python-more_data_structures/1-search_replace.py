#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search in my_list:
        acumulador = 0
        listita = my_list.copy()
        for iterador in my_list:
            if iterador == search:
                listita[acumulador] = replace
            acumulador += 1
    else:
        listita = my_lists
    return listita
