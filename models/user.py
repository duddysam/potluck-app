from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str # TODO: Hash later


class User(UserCreate):     # User class inherits from UserCreate, which does not include an ID.
    id: int