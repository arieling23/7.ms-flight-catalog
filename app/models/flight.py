from sqlalchemy import Column, Integer, String, DateTime
from app.db import Base

class Flight(Base):
    __tablename__ = "flight"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    departure_time = Column(DateTime, nullable=False)
