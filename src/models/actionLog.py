from sqlalchemy import Column, String, Text, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from src.models.base import Base

class ActionLog(Base):
    __tablename__ = 'action_log'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    timestamp = Column(DateTime, default=func.now())
    action = Column(String(300))
    body = Column(Text)
