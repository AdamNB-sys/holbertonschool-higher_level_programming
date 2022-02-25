#!/usr/bin/python3
"""lists all states from hbtn_0e_0_usa database"""

import MySQLdb
from sys import argv


def print_state():
    db = MySQLdb.connect(
        host='localhost', user=argv[1],
        passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    for rows in cur.fetchall():
        print(rows)

    cur.close()
    db.close()


if __name__ == "__main__":
    print_state()
