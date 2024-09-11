from raedyapi import RaedyAPI
from raedyapi.middleware.httpsredirect import HTTPSRedirectMiddleware

app = RaedyAPI()

app.add_middleware(HTTPSRedirectMiddleware)


@app.get("/")
async def main():
    return {"message": "Hello World"}
