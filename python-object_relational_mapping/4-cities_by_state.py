#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, 
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # create cursor object
    cur = db.cursor()
    # execute the query *with parameterized input*
    cur.execute("SELECT * FROM cities ORDER BY id ASC")
    # fecth all rows
    rows = cur.fetchall()
    # print the results
    for row in rows:
        print(row)
    # close the cursor and database connection    
    cur.close()
    db.close()
