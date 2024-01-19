#!/usr/bin/python3
"""Script to connect to a MySQL server and display states using SQLAlchemy."""

import sys
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """Class representing the 'states' table in the database."""

    __tablename__ = 'states'
    id = Column(Integer, Sequence('state_id_seq'), primary_key=True)
    name = Column(String(256), nullable=False)


def main():
    """Connect to MySQL server and display states."""
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    # Create tables if not exists
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve and display states
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("({}, '{}')".format(state.id, state.name))

    # Close the session
    session.close()


if __name__ == "__main__":
    main()
