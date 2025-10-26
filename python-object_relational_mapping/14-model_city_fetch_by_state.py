#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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
    
    # Query all City objects joined with State, ordered by cities.id
    cities = session.query(City, State)\
                   .join(State, City.state_id == State.id)\
                   .order_by(City.id)\
                   .all()
    
    # Display results in the required format
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    
    # Close the session
    session.close()
