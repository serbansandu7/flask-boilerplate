import datetime
import hashlib
from numpy import random

from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey
from sqlalchemy.sql import func

from src.models.base import Base
from src.utils.exceptions import Conflict


class EmailToken(Base):
    __tablename__ = 'email_token'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    token = Column(Text)
    token_create_time = Column(DateTime, default=func.now())

    def generate_email_token(self):
        self.token = hashlib.sha256(random.bytes(2048)).hexdigest()

    @classmethod
    def get_email_token(cls, context, token):
        token = context.query(EmailToken).filter_by(token=token).first()
        if not token:
            raise Conflict("Invalid email token.", 400)

        if token.token_create_time > datetime.datetime.utcnow() + datetime.timedelta(hours=48):
            raise Conflict("The email token has expired", 400)

        return token
