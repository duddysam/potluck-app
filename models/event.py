from pydantic import BaseModel
from datetime import datetime


class EventCreate(BaseModel):
    name: str
    date: datetime
    capacity: int
    
    
class Event(EventCreate):
    id: int
    host_id: int

class CommentCreate(BaseModel):
    text: str
    

class Comment(CommentCreate):
    id: int
    event_id: int
    timestamp: datetime
    posted_by: int
    

