from raedyapi import Depends, RaedyAPI
from raedyapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated

app = RaedyAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
