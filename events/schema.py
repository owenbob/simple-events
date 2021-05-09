
import graphene

from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from events.model import EventsModel


DATE_FORMAT = "%d-%m-%Y"


class EventsType(SQLAlchemyObjectType):
    class Meta:
        model = EventsModel


class SaveEvent(graphene.Mutation):

    class Arguments:
        email = graphene.String()
        environment = graphene.String()
        component = graphene.String()
        message = graphene.String()
        data = graphene.JSONString()

    event = graphene.Field(EventsType)

    def mutate(self, info, **kwargs):
        event = EventsModel(**kwargs)
        event.save()

        return SaveEvent(event=event)


class EventsQuery(graphene.ObjectType):
    events = graphene.List(EventsType)
    events_by_parameters = graphene.List(
        EventsType,
        args={
                "email": graphene.String(),
                "environment": graphene.String(),
                "component": graphene.String(),
                "text": graphene.String(),
                "date": graphene.String()
            }
        )

    def resolve_events(self, info):
        return EventsModel.query.all()

    def resolve_events_by_parameters(self, info, **kwargs):
        email = kwargs.get("email")
        environment = kwargs.get("environment")
        component = kwargs.get("component")
        text = kwargs.get("text")
        date = kwargs.get("date")

        # convert to timestamp
        target_datetime = datetime.strptime(date, DATE_FORMAT)
        target_timestamp = datetime.timestamp(target_datetime)

        results = EventsModel.query.filter(
            EventsModel.email == email,
            EventsModel.environment == environment,
            EventsModel.component == component,
            EventsModel.message.contains(text),
            EventsModel.created_at >= target_timestamp
        )

        return results


class EventsMutation(graphene.ObjectType):
    save_event = SaveEvent.Field()
