from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.database import Base
from datetime import datetime

class Request(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    approved = Column(Boolean, default=False)