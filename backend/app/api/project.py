from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ..models.project import ProjectCreate, Project
from ..services.project_service import ProjectService
from ..db.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/", response_model=Project, status_code=status.HTTP_201_CREATED)
async def create_project(project_in: ProjectCreate, db: AsyncSession = Depends(get_db)):
    service = ProjectService(db)
    try:
        project = await service.create_project(project_in)
        return project
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[Project])
async def list_projects(db: AsyncSession = Depends(get_db)):
    service = ProjectService(db)
    projects = await service.list_projects()
    return projects
