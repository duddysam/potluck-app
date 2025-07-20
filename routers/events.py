from fastapi import APIRouter
from models.event import EventCreate, Event, CommentCreate, Comment
from database.memory import events_db, users_db, comments_db, get_next_comment_id,  get_next_event_id
from datetime import datetime

router = APIRouter(prefix="/events", tags=["users"])

@router.post("/create/{host_id}", response_model=Event)
def create_event(host_id: int, event: EventCreate):
    if host_id not in users_db:
        return {"message": "host id is invalid"}
    event_id = get_next_event_id()
    event_dict = event.model_dump()
    event_dict['host_id'] = host_id
    event_dict['id'] = event_id
    event_dict['comments'] = []
    events_db[event_id] = event_dict
    return event_dict

@router.get("/")
def get_events():
    return list(events_db.values())

@router.post("/{event_id}/create-comment/{posted_by}", response_model=Comment)
def event_create_comment(event_id: int, posted_by: int, comment: CommentCreate):

    if event_id not in events_db:
        return {"message": "no event was found."}

    if posted_by not in users_db:
        return {"message": "invalid user ID."}

    else:
        comment_id = get_next_comment_id()
        comment_dict = comment.model_dump()
        comment_dict['event_id'] = event_id
        comment_dict['posted_by'] = posted_by
        comment_dict['id'] = comment_id
        comment_dict['timestamp'] = datetime.now()
        comments_db[comment_id] = comment_dict
        events_db[event_id]['comments'].append(comment_dict)
        return comment_dict