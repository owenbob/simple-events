"""
Configure database.
"""

from config.config import application_configuration
from common.utilities import generate_uuid
from common.custom_types import TimestampType
from sqlalchemy import Column, String
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


def create_db_session():
    """
    Create database session.
    """
    database_uri = application_configuration.DATABASE_URI
    engine = create_engine(database_uri)
    session = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
    return scoped_session(session)


Base = declarative_base()
db_session = create_db_session()
Base.query = db_session.query_property()


class BaseModel(Base):

    __abstract__ = True
    id = Column(String, primary_key=True, default=generate_uuid)
    created_at = Column(TimestampType)

    def save(self):
        """default save method."""
        db_session.add(self)
        db_session.commit()
