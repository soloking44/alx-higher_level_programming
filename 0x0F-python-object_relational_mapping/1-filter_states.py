#!/usr/bin/python3
"""
A code is required to display all states whose names begin with uppercase
letter "N" from the "hbtn_0e_0_usa database.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    query = "SELECT * FROM states\
             WHERE states.name LIKE BINARY 'N%'\
             ORDER BY states.id ASC"
    cursor = db.cursor()
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
