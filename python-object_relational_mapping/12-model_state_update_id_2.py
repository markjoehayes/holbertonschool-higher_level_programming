#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
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
    
    # Query for the State object with id = 2
    state = session.query(State).filter(State.id == 2).first()
    
    # If state is found, update its name
    if state:
        state.name = "New Mexico"
        # Commit the changes to the database
        session.commit()
    
    # Close the session
    session.close()
