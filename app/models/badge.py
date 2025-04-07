from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

class Badge(Base):
    __tablename__ = "badges"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)  # bronze, silver, gold
    awarded_at = Column(DateTime, default=datetime.utcnow)