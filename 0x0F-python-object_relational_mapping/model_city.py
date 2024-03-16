#!/usr/bin/python3
"""It has an explanation of a State with class instance
Base = declarative_base() """


from sqlalchemy import Column, Integer, String
from model_state import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey


class City(Base):
    """ This city is fetch within the database and 
    connects class to a state table.
    Attr:
        id, name
    """
__tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
