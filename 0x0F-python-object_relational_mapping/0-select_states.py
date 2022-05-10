#!/usr/bin/python
"""Conectamos con la bd, usamos cursor para generar el entorno de trabajo,
seguido usamos el execute para generar la consulta y con fetchall obtenemos el
resultado"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC;')
    rows = cur.fetchall()
    for fila in rows:
        print fila
