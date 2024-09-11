from raedyapi import RaedyAPI
from raedyapi.responses import PlainTextResponse

app = RaedyAPI()


@app.get("/", response_class=PlainTextResponse)
async def main():
    return "Hello World"
