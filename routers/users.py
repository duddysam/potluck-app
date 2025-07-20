from fastapi import APIRouter
from models.user import UserCreate, User
from database.memory import users_db, get_next_user_id

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=User) # This specifices that the return is User (which has ID)
def register_user(user: UserCreate): # This specifies that the function param is UserCreate (which omits ID)
    user_id = get_next_user_id()
    user_dict = user.model_dump()
    user_dict['id'] = user_id
    users_db[user_id] = user_dict
    return user_dict

@router.get('/')
def get_users():
    return list(users_db.values())