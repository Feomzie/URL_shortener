from sqlalchemy import Column, Integer, String, DateTime, func 
from app.db.database import Base


class ShortURL(Base):
    __tablename__ = "short_urls"

    id = Column(Integer, primary_key=True)
    original_url = Column(String, nullable=False)
    short_url = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())