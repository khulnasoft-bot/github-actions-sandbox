from raedyapi import RaedyAPI

app = RaedyAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}
