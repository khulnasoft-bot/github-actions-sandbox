from raedyapi import RaedyAPI

my_awesome_api = RaedyAPI()


@my_awesome_api.get("/")
async def root():
    return {"message": "Hello World"}
