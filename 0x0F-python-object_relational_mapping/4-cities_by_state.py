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
        database=argv[3]
    )
    cursor = connection.cursor()
    cursor.execute(""" SELECT
                    cities.id,
                    cities.name,
                    states.name
                    FROM
                    cities
                    JOIN
                    states
                    ON
                    cities.state_id = states.id
                    ORDER BY id ASC""")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()
