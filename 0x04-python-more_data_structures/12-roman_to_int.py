#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    if roman_string and isinstance(roman_string, str):
        values = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        anterior = 0
        for iterador in roman_string[::-1]:
            valor = values[iterador]
            if valor >= anterior:
                total += valor
            else:
                total -= valor
            anterior = valor
    return total
