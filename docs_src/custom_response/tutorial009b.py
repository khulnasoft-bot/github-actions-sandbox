from raedyapi import RaedyAPI
from raedyapi.responses import FileResponse

some_file_path = "large-video-file.mp4"
app = RaedyAPI()


@app.get("/", response_class=FileResponse)
async def main():
    return some_file_path
