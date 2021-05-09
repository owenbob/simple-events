
from datetime import datetime
from uuid import uuid4


def generate_uuid():
    """
    Return a string uuid.
    """
    return str(uuid4())


def current_timestamp():
    """Generate current utc timestamp."""
    current_datetime = datetime.utcnow()
    timestamp = datetime.timestamp(current_datetime)
    return timestamp
