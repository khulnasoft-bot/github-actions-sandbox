from functools import lru_cache

from raedyapi import Depends, RaedyAPI
from typing_extensions import Annotated

from .config import Settings

app = RaedyAPI()


@lru_cache()
def get_settings():
    return Settings()


@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }
