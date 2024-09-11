from typing import Dict

from raedyapi import RaedyAPI

app = RaedyAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights
