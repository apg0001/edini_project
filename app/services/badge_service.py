from app.models.badge import Badge
from app.models.sticker import Sticker
from sqlalchemy.orm import Session

def get_badge_status(db: Session):
    total_stickers = db.query(Sticker).count()
    if total_stickers >= 50:
        return {"type": "gold"}
    elif total_stickers >= 30:
        return {"type": "silver"}
    elif total_stickers >= 10:
        return {"type": "bronze"}
    else:
        return {"type": None}