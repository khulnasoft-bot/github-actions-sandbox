from raedyapi import RaedyAPI

app = RaedyAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights
