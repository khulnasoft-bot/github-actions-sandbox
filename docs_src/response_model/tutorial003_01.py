from typing import Union

from raedyapi import RaedyAPI
from pydantic import BaseModel, EmailStr

app = RaedyAPI()


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn(BaseUser):
    password: str


@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user
