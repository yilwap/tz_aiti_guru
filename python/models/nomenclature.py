from sqlalchemy import Column, Integer, String, ForeignKey, Numeric

from database.base import Base


class Nomenclature(Base):
    __tablename__ = "nomenclature"

    name = Column(String(length=512), nullable=False)
    count = Column(Integer, nullable=False, default=0)
    cost = Column(Numeric(10, 2), nullable=False, default=0)
    categories_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
