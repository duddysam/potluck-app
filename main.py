from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    password: str
    id: int
    firstName: str
    lastName: str
    #friends:
    #events:


@app.get("/")
def index():
    return "hello potluck!"

@app.post("/users/register")
def register_user(user: User):

    # TODO: save to DB later

    return {"message": "User registered", "user": user.username}