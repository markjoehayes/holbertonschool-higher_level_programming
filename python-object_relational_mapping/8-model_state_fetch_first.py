#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import State and Base from model_state
try:
    from model_state import Base, State
except ImportError:
    # If direct import fails, try alternative approach
    import os
    import importlib.util
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_state_path = os.path.join(current_dir, 'model_state.py')
    
    if os.path.exists(model_state_path):
        spec = importlib.util.spec_from_file_location("model_state", model_state_path)
        model_state = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(model_state)
        State = model_state.State
        Base = model_state.Base
    else:
        print("Error: model_state.py not found")
        sys.exit(1)

if __name__ == "__main__":
    # Get command line arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)
        
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    try:
        # Create engine and connect to database
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database),
            pool_pre_ping=True
        )
        
        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)
        
        # Create a Session instance
        session = Session()
        
        # Query the first State object ordered by id
        first_state = session.query(State).order_by(State.id).first()
        
        # Display result
        if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")
        
        # Close the session
        session.close()
        
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
