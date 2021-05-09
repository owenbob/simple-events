

# Create events application
from graphene import Schema

from events.schema import EventsQuery, EventsMutation
from common.app_creation import create_app
from config.config import application_configuration


"""
--- Expanding Business Logic ---
By using the AllQueries and AllMutations classes we are
able to add other query and mutation classes.

This enables us to create other modules/components/apps with their own
queries and mutation and then combine them to create one schema
for the service for example we can create a payments module/component/app:

from payment.schema import PaymentsQuery, PaymentMutation
from events.schema import EventsQuery, EventsMutation

class AllQueries(EventsQuery, PaymentsQuery):
    pass


class AllMutations(EventsMutation, PaymentMutation):
    pass

We would then use these to create the schema.

this would be done in a `service.py` in the root directory
"""


class AllQueries(EventsQuery):
    pass


class AllMutations(EventsMutation):
    pass


events_schema = Schema(query=AllQueries, mutation=AllMutations)

events_config = application_configuration
events_app = create_app(
    schema=events_schema,
    config=events_config
)
