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
    command = """SELECT
                cities.name
                FROM
                cities
                JOIN
                states
                ON
                cities.state_id = states.id
                WHERE
                states.name LIKE '{:s}'
                ORDER BY cities.id ASC""".format(argv[4])
    cursor.execute(command)
    city_names = []
    for row in cursor.fetchall():
        city_names.append(row[0])
    result = ", ".join(city_names)
    print(result)
    cursor.close()
    connection.close()
