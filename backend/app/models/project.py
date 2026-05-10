from pydantic import BaseModel, Field
from datetime import datetime

class ProjectCreate(BaseModel):
    title: str = Field(..., max_length=200)
    description: str | None = None
    start_date: datetime
    end_date: datetime | None = None
    pi_id: int
    budget: float

class ProjectOut(BaseModel):
    id: int
    title: str
    description: str | None
    start_date: datetime
    end_date: datetime | None
    pi_id: int
    budget: float
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
