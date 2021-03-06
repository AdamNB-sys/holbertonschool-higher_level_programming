#!/usr/bin/python3
"""lists states starting with capital N from hbtn_0e_0_usa"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    for row in states:
        if row[1][0] == 'N':
            print(row)

    cur.close()
    db.close()
