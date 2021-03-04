import logging

import settings
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database_session = None


def build_connection_string(host, username, password, port, database):
    return f'postgresql://{username}:{password}@{host}:{port}/{database}'


def create_dependent_tables(engine):
    from src.models.base import Base
    from src.models.user import User
    Base.metadata.create_all(engine)


def init_database_connection(connection_string):
    global database_session

    if not database_exists(connection_string):
        create_database(connection_string)

    engine = sqlalchemy.create_engine(connection_string, pool_size=90, max_overflow=10, pool_recycle=3600)
    database_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    create_dependent_tables(engine)
    logger.info('Successful initiated the database')
    return engine, database_session
