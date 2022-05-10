#!/usr/bin/python
"""Lo mismo solo que en este caso mandamos el parametro numero 4 para hacer la
consulta"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cu = db.cursor()
    cu.execute('SELECT * FROM states WHERE name LIKE %(fil)s ORDER BY id ASC;',
               {'fil': sys.argv[4]})
    rows = cu.fetchall()
    for fila in rows:
        print fila
