from raedyapi import RaedyAPI
from raedyapi.middleware.gzip import GZipMiddleware

app = RaedyAPI()

app.add_middleware(GZipMiddleware, minimum_size=1000)


@app.get("/")
async def main():
    return "somebigcontent"
