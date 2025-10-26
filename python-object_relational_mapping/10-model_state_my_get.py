#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
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
    state_name = sys.argv[4]
    
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
    
    # Query for the state with the exact name (SQL injection free using parameterized query)
    state = session.query(State).filter(State.name == state_name).first()
    
    # Display result
    if state:
        print(state.id)
    else:
        print("Not found")
    
    # Close the session
    session.close()
