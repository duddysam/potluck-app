from fastapi import APIRouter
from models.event import EventCreate, CommentCreate
from database.memory import events_db, comments_db, get_next_comment_id,  get_next_event_id

router = APIRouter(prefix="/events", tags=["users"])

@router.post("/create")
def create_event(event: EventCreate):
    event_id = get_next_event_id()
    event_dict = event.model_dump()
    event_dict['id'] = event_id
    events_db[event_id] = event_dict
    return event_dict

@router.post("/{event_id}/create-comment/")
def event_create_comment(event_id: int, comment: CommentCreate):

    if event_id not in events_db:
        return {"message": "no event was found."}

    else:
        comment_id = get_next_comment_id()
        comment_dict = comment.model_dump()
        comment_dict['event_id'] = event_id
        comment_dict['id'] = comment_id
        comments_db[comment_id] = comment_dict
        return comment_dict