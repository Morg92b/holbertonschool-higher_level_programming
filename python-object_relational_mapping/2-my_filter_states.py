#!/usr/bin/python3

"""script that takes in an argument and displays all values,
in the states table of hbtn_0e_0_usa where name matches the argument"""

import sys
import MySQLdb

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states \
        WHERE name = '{}' ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
