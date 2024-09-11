from typing import Dict

from raedyapi import RaedyAPI

app = RaedyAPI()


@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}
