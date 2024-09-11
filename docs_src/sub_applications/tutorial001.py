from raedyapi import RaedyAPI

app = RaedyAPI()


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}


subapi = RaedyAPI()


@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}


app.mount("/subapi", subapi)
