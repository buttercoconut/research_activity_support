from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models.project_db import Project as ProjectDB
from ..models.project import ProjectCreate, Project

class ProjectService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_project(self, project_in: ProjectCreate) -> Project:
        db_project = ProjectDB(**project_in.dict())
        self.db.add(db_project)
        await self.db.commit()
        await self.db.refresh(db_project)
        return Project.from_orm(db_project)

    async def list_projects(self) -> list[Project]:
        result = await self.db.execute(select(ProjectDB))
        projects = result.scalars().all()
        return [Project.from_orm(p) for p in projects]
