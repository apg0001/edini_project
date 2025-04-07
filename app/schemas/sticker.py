from pydantic import BaseModel
from datetime import date

class StickerCreate(BaseModel):
    date: date
    reason: str
    count: int = 1
    source: str = "admin"

class StickerOut(BaseModel):
    date: date
    reason: str
    count: int