#!/usr/bin/python3
"""Class State."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    all = session.query(State.id, State.name, City.id, City.name)\
        .join(City).all()
    for city in all:
        print("{:d}: ({:s}) >> {:d}: ({:s})"
              .format(city[0], city[1], city[2], city[3]))
    session.close()
