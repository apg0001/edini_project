from pydantic import BaseModel
from datetime import datetime

class RequestCreate(BaseModel):
    message: str

class RequestResponse(BaseModel):
    id: int
    message: str
    date_created: datetime
    approved: bool