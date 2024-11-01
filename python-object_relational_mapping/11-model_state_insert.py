#!/usr/bin/python3

"""script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""

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

    add_state = State(name='Louisiana')
    session.add(add_state)
    session.commit()
    print('{}'.format(add_state.id))

    session.close()
