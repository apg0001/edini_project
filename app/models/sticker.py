from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Sticker(Base):
    __tablename__ = "stickers"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    reason = Column(String)
    count = Column(Integer, default=1)
    source = Column(String, default="admin")  # admin or request