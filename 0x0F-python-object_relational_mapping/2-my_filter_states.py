#!/usr/bin/python3
"""Lo mismo solo que en este caso mandamos el parametro numero 4 para hacer la
consulta"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cu = db.cursor()
    cu.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".
               format(argv[4]))
    rows = cu.fetchall()
    for fila in rows:
        print(fila)
    cu.close()
    db.close()
