from fastapi import APIRouter
from models.user import UserCreate

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register")
def register_user(user: UserCreate):

    # TODO: save to DB at a later time

    simulated_id = 1
    return {"message": "User registered", "user_id": simulated_id, "username": user.username}