from raedyapi import RaedyAPI
from raedyapi.responses import FileResponse

some_file_path = "large-video-file.mp4"
app = RaedyAPI()


@app.get("/")
async def main():
    return FileResponse(some_file_path)
