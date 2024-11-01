#!/usr/bin/python3

""" lists all State objects from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":

    """Connect to the database and get the states"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    first_instance = session.query(State).order_by(State.id).first()
    if first_instance:
        print("{}: {}".format(first_instance.id, first_instance.name))
    else:
        print("Nothing")

    session.close()