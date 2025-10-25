#!/usr/bin/python3
import MySQLdb
import sys

"""
Script that lists all states from the database hbtn_0e_0_usa
"""

def list_states(username, password, db_name):
    """Connects to MySQL db and lists all states, sorted by id"""
    # Connect to the MySQL database
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=db_name
    )

    # create a cursor object
    cursor = db.cursor()

    # execute the SQL query
    cursor.execute('SELECT * FROM states ORDER by id ASC')

    # Fetch all the rows
    states = cursor.fetchall()

    # print each state
    for state in states:
        print(state)

    # close the cursor and db connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # get command line args
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Call the function to list states
    list_states(username, password, db_name)

