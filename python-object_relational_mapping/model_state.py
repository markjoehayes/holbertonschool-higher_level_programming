#!/usr/bin/python3
"""
State class definition and Base instance
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create declarative base instance
Base = declarative_base()

class State(Base):
    """
    State class that links to the MySQL table 'states'
    """
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    import sys
    
    # Create connection string and engine
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )
    
    # Create all tables
    Base.metadata.create_all(engine)
