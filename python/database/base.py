from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

DataBase = declarative_base()


class Base(DataBase):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
