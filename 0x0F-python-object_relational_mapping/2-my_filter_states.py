#!/usr/bin/python3
"""Script."""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3],
    )
    cursor = connection.cursor()
    command = """SELECT *
                FROM states
                WHERE name LIKE '{:s}' ORDER BY id ASC""".format(argv[4])
    cursor.execute(command)
    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    connection.close()
