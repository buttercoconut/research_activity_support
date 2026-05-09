from pydantic import BaseModel, Field
from datetime import date

class ProjectBase(BaseModel):
    title: str = Field(..., example="AI 기반 학습 분석")
    description: str | None = Field(None, example="학생 학습 데이터를 분석하여 맞춤형 피드백 제공")
    start_date: date = Field(..., example="2024-01-01")
    end_date: date | None = Field(None, example="2024-12-31")
    budget: float = Field(..., example=5000000.0)

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True
