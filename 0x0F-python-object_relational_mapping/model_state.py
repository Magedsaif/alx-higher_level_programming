from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_6_usa')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class State(Base):
    """Class."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(129), nullable=False)


Base.metadata.create_all(engine)
