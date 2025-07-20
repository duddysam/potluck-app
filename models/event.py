from pydantic import BaseModel
from datetime import datetime


class EventCreate(BaseModel):
    name: str
    date: datetime
    host_id: int
    capacity: int
    id: int
    # guest_list
    # comments
    # dishes

class CommentCreate(BaseModel):
    id: int
    event_id: int
    text: str
    date: datetime
    posted_by: int

