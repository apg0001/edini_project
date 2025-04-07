from pydantic import BaseModel
from datetime import datetime

class BadgeOut(BaseModel):
    type: str
    awarded_at: datetime