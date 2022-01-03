#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    else:
        compar = my_list[0]
        for iterador in my_list:
            if iterador > compar:
                compar = iterador
    return (compar)
