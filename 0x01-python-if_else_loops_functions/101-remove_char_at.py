#!/usr/bin/python3
def remove_char_at(str, n):
    cualquiera = ""
    if len(str) >= n and n >= 0:
        for numerito in str:
            if str[n] != numerito:
                cualquiera = cualquiera + numerito
    else:
        cualquiera = str
    return(cualquiera)
