from typing import Union

from raedyapi import RaedyAPI
from pydantic import BaseModel, EmailStr

app = RaedyAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


# Don't do this in production!
@app.post("/user/")
async def create_user(user: UserIn) -> UserIn:
    return user
