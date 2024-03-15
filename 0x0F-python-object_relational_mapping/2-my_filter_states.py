#!/usr/bin/python3
"""
A code is needed to accept an argument and show all entries within
"states" table of hbtn_0e_0_usa where name hits the provided.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    query = "SELECT * FROM states\
             WHERE states.name LIKE BINARY '{}'\
             ORDER BY states.id ASC".format(sys.argv[4])
    cursor = db.cursor()
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
