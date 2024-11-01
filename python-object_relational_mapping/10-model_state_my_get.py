#!/usr/bin/python3

"""script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":

    """Connect to the database"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    """Add argv for search with name the state"""
    instance = session.query(State).filter(State.name == sys.argv[4]).first()

    if instance is None:
        print("Not found")
    else:
        print("{}".format(instance.id))

    session.close()
