import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime

from src.adapters.user import UserAdapter
from src.models.base import Base
from src.models.crud import Crud
from src.utils.exceptions import InvalidCredentials, Conflict
from src.utils.validators import validate_user_body


class User(Base, Crud, UserAdapter):
    search_fields = ['email', 'first_name', 'last_name']
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    phone = Column(String(15))
    admin = Column(Boolean, default=False)
    active = Column(Boolean, default=True)
    password = Column(String(500), nullable=False)
    salt = Column(String(500))
    session = Column(String(1024))
    session_create_time = Column(DateTime)

    @classmethod
    def get_search_fields(cls):
        return cls.search_fields

    @classmethod
    def get_users(cls, context, search, page, limit):
        query = context.query(cls)
        query = cls.add_search(query, search)
        total = query.count()
        query = cls.add_pagination(query, page, limit)
        results = query.all()
        return cls.to_json(results, total)

    @classmethod
    def login(cls, context, body):
        user = cls.get_user_by_email(context, body.get("email"))
        if not user:
            raise InvalidCredentials("User not found", status=400)

        password, _ = cls.generate_password(body.get("password"), user.salt.encode('utf-8'))
        if password != user.password:
            raise InvalidCredentials("Invalid credentials", status=400)
        session_token = cls.generate_session()
        user.session = session_token
        user.session_create_time = datetime.datetime.now()
        context.commit()
        return session_token

    @classmethod
    def logout(cls, context, session_id):
        user = cls.get_user_by_session(context, session_id)
        if not user:
            raise InvalidCredentials("User not found", status=400)
        user.session = None
        context.commit()

    @classmethod
    def get_user_by_email(cls, context, email):
        return context.query(cls).filter_by(email=email).first()

    @classmethod
    def get_user_by_session(cls, context, session):
        return context.query(cls).filter_by(session=session).first()

    @classmethod
    def get_user_by_id(cls, context, user_id):
        return context.query(cls).filter_by(id=user_id).first()

    @classmethod
    def create_user(cls, context, body):
        validate_user_body(body)
        if cls.get_user_by_email(context, body.get("email")):
            raise Conflict("This email address is already used", 409)
        user = User()
        user.to_object(body)
        context.add(user)
        context.commit()

    @classmethod
    def update_user(cls, context, body, user_id):
        validate_user_body(body)
        user = cls.get_user_by_id(context, user_id)
        if not user:
            raise Conflict("The user you are trying to update does not exist", 404)
        user.to_object(body)
        context.commit()

    @classmethod
    def deactivate_user(cls, context, user_id):
        user = cls.get_user_by_id(context, user_id)
        if not user:
            raise Conflict("The user you are trying to update does not exist", 404)
        user.active = False
        context.commit()
