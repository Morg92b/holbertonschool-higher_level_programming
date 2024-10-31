#!/usr/bin/python3

"""Class states and instance of base = declarative_base"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class States"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
