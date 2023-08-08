from sqlalchemy import Column, Integer, String
from database import Base


class Item(Base):
    __tablename__ = 'items'
    id = Column(String(256), primary_key=True)
    status = Column(String(256))
