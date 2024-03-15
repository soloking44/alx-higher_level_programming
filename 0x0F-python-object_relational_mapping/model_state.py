#!/usr/bin/python3
"""This code has an explanation of class called State with an example instance.
Base = declarative_base() """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ This class is fetch within the database and
    connects class to a table.
    Attr:
        id, name
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
