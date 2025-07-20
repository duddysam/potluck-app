from fastapi import APIRouter
from models.event import EventCreate, CommentCreate

router = APIRouter(prefix="/events", tags=["users"])

@router.post("/create")
def create_event(event: EventCreate):

    return{"message": "Event created", "event_name": event.name, "event_date": event.date}

@router.post("/create-comment/")
def event_create_comment(comment: CommentCreate):
    return {"message": "Comment created", "comment_text": comment.text, "created_by": comment.posted_by}