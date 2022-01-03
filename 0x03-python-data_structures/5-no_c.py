#!/usr/bin/env python3
def no_c(my_string):
    sinC = ""
    for iterador in my_string:
        if iterador not in "Cc":
            sinC = sinC + iterador
    return (sinC)
