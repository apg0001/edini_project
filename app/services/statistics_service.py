from app.models.sticker import Sticker
from sqlalchemy.orm import Session
from collections import defaultdict

def get_monthly_statistics(db: Session):
    result = defaultdict(int)
    stickers = db.query(Sticker).all()
    for s in stickers:
        key = s.date.strftime("%Y-%m")
        result[key] += s.count
    return dict(result)