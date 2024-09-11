from raedyapi import RaedyAPI
from pydantic import BaseModel, HttpUrl

app = RaedyAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images
