from sqlalchemy import Column, String

from database.base import Base


class Clients(Base):
    __tablename__ = "clients"

    name = Column(String(length=512), nullable=False)
    address = Column(String(length=512), nullable=False)
