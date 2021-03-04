from sqlalchemy import Column, ForeignKey, Integer, String

from .base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(500))
    role = Column(String(500))
    password = Column(String(500))
    user_full_name = Column(String(500))
    location = Column(Integer, ForeignKey('locations.id'))
