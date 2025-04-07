from app.models.sticker import Sticker
from app.schemas.sticker import StickerCreate
from sqlalchemy.orm import Session

def give_sticker(db: Session, sticker_data: StickerCreate):
    sticker = Sticker(**sticker_data.dict())
    db.add(sticker)
    db.commit()
    db.refresh(sticker)
    return sticker

def get_calendar_data(db: Session):
    return db.query(Sticker).all()