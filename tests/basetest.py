import sys
import os

from graphene.test import Client
from unittest import TestCase
from common.base_model import Base, db_session
from config.config import application_configuration
from events import events_schema
from sqlalchemy.engine import create_engine
from tests.fixtures import seed_test_events_query

sys.path.append(os.getcwd())


class BaseTestCase(TestCase):
    database_uri = application_configuration.DATABASE_URI
    engine = create_engine(database_uri)

    def setUp(self):
        Base.metadata.create_all(self.engine)
        self.test_client = Client(schema=events_schema)
        self.test_client.execute(seed_test_events_query)

    def tearDown(self):
        db_session.remove()
        Base.metadata.drop_all(bind=self.engine)
