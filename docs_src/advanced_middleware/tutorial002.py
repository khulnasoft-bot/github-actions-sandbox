from raedyapi import RaedyAPI
from raedyapi.middleware.trustedhost import TrustedHostMiddleware

app = RaedyAPI()

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com"]
)


@app.get("/")
async def main():
    return {"message": "Hello World"}
