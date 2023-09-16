#!/usr/bin/python3
"""Class State."""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Class."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_6_usa')
Base.metadata.create_all(engine)
