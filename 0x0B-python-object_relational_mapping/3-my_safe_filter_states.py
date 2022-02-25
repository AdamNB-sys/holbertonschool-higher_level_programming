#!/usr/bin/python3
"""takes an argument and returns matching results from
the hbtn_0e_0_usa database
injection proof"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name\
        LIKE binary %s", (argv[4],))
    states = cur.fetchall()
    for row in states:
        print(row)

    cur.close()
    db.close()
