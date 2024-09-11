from typing import Annotated

from raedyapi import Depends, RaedyAPI
from raedyapi.security import HTTPBasic, HTTPBasicCredentials

app = RaedyAPI()

security = HTTPBasic()


@app.get("/users/me")
def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"username": credentials.username, "password": credentials.password}
