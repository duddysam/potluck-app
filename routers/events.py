from fastapi import APIRouter
from models.event import EventCreate

router = APIRouter(prefix="/events", tags=["users"])

@router.post("/create")
def create_event(event: EventCreate):

    return{"message": "Event created", "event_name": event.name, "event_date": event.date}