from sqlalchemy import Column, Integer, String, ForeignKey

from database.base import Base


class Categories(Base):
    __tablename__ = "categories"

    name = Column(String(length=512), nullable=False)
    parent_categories_id = Column(Integer, ForeignKey("categories.id"))
    materialize_path = Column(String, unique=True)
