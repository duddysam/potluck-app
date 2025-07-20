from fastapi import APIRouter
from models.user import UserCreate
from database.memory import users_db, user_id_counter, get_next_user_id

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register")
def register_user(user: UserCreate):
    user_id = get_next_user_id()
    user_dict = user.model_dump()
    user_dict['id'] = user_id
    users_db[user_id] = user_dict
    return user_dict