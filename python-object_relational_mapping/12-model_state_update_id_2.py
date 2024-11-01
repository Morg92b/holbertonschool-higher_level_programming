#!/usr/bin/python3

"""script that changes the name of a State object
from the database hbtn_0e_6_usa"""

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

    update_state = session.query(State).filter_by(id=2).first()
    update_state.name = "New Mexico"

    session.commit()
    session.close()
