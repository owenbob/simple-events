
import sqlalchemy.types as types

from common.utilities import current_timestamp


class TimestampType(types.TypeDecorator):
    impl = types.Integer
    cache_ok = True

    def process_bind_param(self, value, dialect):
        return current_timestamp()
