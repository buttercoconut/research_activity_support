from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    budget = Column(Float, nullable=False)
    created_at = Column(Date, default=Date.utcnow)
    updated_at = Column(Date, default=Date.utcnow, onupdate=Date.utcnow)
