"""
The events model.
"""

from common.base_model import BaseModel
from sqlalchemy import Column, String, JSON


class EventsModel(BaseModel):
    __tablename__ = 'events'
    email = Column(String)
    environment = Column(String)
    component = Column(String)
    message = Column(String)
    data = Column(JSON)
