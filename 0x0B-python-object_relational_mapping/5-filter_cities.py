#!/usr/bin/python3
"""lists all cities that belong to a given state
from the database hbtn_0e_4_usa"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities LEFT JOIN states ON\
        cities.state_id=states.id WHERE states.name LIKE %s ORDER BY\
            cities.id;", [format(argv[4])])
    cities = cur.fetchall()
    print(", ".join(row[0] for row in cities))

    cur.close()
    db.close()
