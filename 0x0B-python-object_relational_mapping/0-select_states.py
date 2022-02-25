#!/usr/bin/python3
"""lists all states from hbtn_0e_0_usa database"""
import MySQLdb
from sys import argv


def main():
    db = MySQLdb.connect(
        host='localhost', port=3306, user=argv[1],
        passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for row in states():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
