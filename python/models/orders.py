from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database.base import Base


class Orders2Nomenclature(Base):
    __tablename__ = "orders2nomenclature"

    orders_id = Column(Integer, ForeignKey("orders.id"), primary_key=True)
    nomenclature_id = Column(Integer, ForeignKey("nomenclature.id"), primary_key=True)
    count = Column(Integer, default=1, nullable=False)

    nomenclature = relationship(
        "Nomenclature",
        lazy="selectin",
        viewonly=True,
    )


class Orders(Base):
    __tablename__ = "orders"

    clients_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    created_date = Column(
        DateTime, default=datetime.now, server_default="NOW()", nullable=False
    )

    nomenclature = relationship(
        "Nomenclature",
        secondary=Orders2Nomenclature.__table__,
        lazy="selectin",
        viewonly=True,
    )

    clients = relationship(
        "Clients",
        lazy="selectin",
        viewonly=True,
    )

    orders2nomenclature = relationship(
        "Orders2Nomenclature",
        lazy="selectin",
        viewonly=False,
        backref="order",
    )
