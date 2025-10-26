#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Create engine and connect to database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query all State objects that contain the letter 'a', ordered by id
    states = session.query(State)\
                   .filter(State.name.like('%a%'))\
                   .order_by(State.id)\
                   .all()
    
    # Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))
    
    # Close the session
    session.close()
