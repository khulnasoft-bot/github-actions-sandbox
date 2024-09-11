from raedyapi import RaedyAPI
from raedyapi.responses import StreamingResponse

some_file_path = "large-video-file.mp4"
app = RaedyAPI()


@app.get("/")
def main():
    def iterfile():  # (1)
        with open(some_file_path, mode="rb") as file_like:  # (2)
            yield from file_like  # (3)

    return StreamingResponse(iterfile(), media_type="video/mp4")
