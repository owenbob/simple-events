"""
Module to handle creation of multiple app instances.
"""

from flask import Flask
from flask_graphql import GraphQLView


def create_app(schema, config):
    """
    Create app instance.
    params:
        - schema : graphql schema eg events_schema
        - config : configuration specification for this application
    """
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=config.DATABASE_URI,
        DEBUG=config.DEBUG,
        SECRET_KEY=config.SECRET_KEY,
        SQLALCHEMY_TRACK_MODIFICATIONS=config.SQLALCHEMY_TRACK_MODIFICATIONS
    )
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )

    return app
