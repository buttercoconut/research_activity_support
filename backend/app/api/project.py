from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_db
from ..models.project import ProjectCreate, ProjectOut
from ..services.project_service import ProjectService

router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/", response_model=ProjectOut, status_code=status.HTTP_201_CREATED)
async def create_project(project_in: ProjectCreate, db: AsyncSession = Depends(get_db)):
    service = ProjectService(db)
    try:
        project = await service.create_project(project_in)
        return project
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{project_id}", response_model=ProjectOut)
async def read_project(project_id: int, db: AsyncSession = Depends(get_db)):
    service = ProjectService(db)
    try:
        return await service.get_project(project_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[ProjectOut])
async def list_projects(db: AsyncSession = Depends(get_db)):
    service = ProjectService(db)
    return await service.list_projects()
