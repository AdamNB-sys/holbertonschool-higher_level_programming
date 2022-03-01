#!/usr/bin/python3


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id = states.id;")
    cities = cur.fetchall()
    for row in cities:
        print(row)

    cur.close()
    db.close()
