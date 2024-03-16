#!/usr/bin/python3
"""
It has the explanation of the city within a class.
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    It explains all city within a class.
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
