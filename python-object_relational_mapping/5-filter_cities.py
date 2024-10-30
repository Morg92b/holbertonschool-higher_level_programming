#!/usr/bin/python3

"""script that takes in the name of a state
as an argument and lists all cities of that state"""

import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = connection.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name \
        FROM cities \
        INNER JOIN states \
        ON cities.state_id = states.id \
        WHERE states.name = %s \
        ORDER BY cities.id ASC",
        (sys.argv[4],)
    )
    rows = cursor.fetchall()
    print(", ".join([row[1] for row in rows]))

    cursor.close()
    connection.close()
