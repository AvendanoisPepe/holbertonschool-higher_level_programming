#!/usr/bin/python3
"""lo mismo que el anterior solo que ahora unamos LIKE para mostrar todos los
resultados que comiences con N"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
                )
    rows = cur.fetchall()
    for fila in rows:
        if fila[1][0] == "N":
            print(fila)
    cur.close()
    db.close()
