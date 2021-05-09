
"""Configuration File."""
import os


class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class EventsDevelopmentConfig(Config):

    DEBUG = True
    DATABASE_URI = os.getenv("EVENTS_DEV_DATABASE_URI")
    SECRET_KEY = os.getenv("EVENTS_APP_SECRET")


class EventsTestingConfig(Config):
    DATABASE_URI = os.getenv("EVENTS_TEST_DATABASE_URI")
    EVENTS_SECRET_KEY = os.getenv("EVENTS_APP_SECRET")
    SECRET_KEY = os.getenv("EVENTS_APP_SECRET")


class EventsProductionConfig(Config):
    DATABASE_URI = os.getenv("EVENTS_PROD_DATABASE_URI")
    SECRET_KEY = os.getenv("EVENTS_APP_SECRET")


def set_config():

    services = {
        "events": {
            "dev": EventsDevelopmentConfig(),
            "test": EventsTestingConfig(),
            "prod": EventsProductionConfig()
        }
    }

    # Make events the default service
    target_service = os.getenv("TARGET_SERVICE", "events")

    # Make dev environment the default if there is no ENV variable set
    target_env = os.getenv("ENV", "dev")

    return services.get(target_service).get(target_env)


application_configuration = set_config()
