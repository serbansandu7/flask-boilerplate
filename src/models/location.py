from sqlalchemy import Column, Integer, String

from .base import Base


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    city = Column(String(500))
    street = Column(String(500))
    street_no = Column(Integer)
    zip_code = Column(Integer)
