from pydantic import BaseModel
from datetime import datetime


class EventCreate(BaseModel):
    name: str
    date: datetime
    host_id: int
    capacity: int
    # guest_list
    # comments
    # dishes