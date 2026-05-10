from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound

from .project_db import Project
from ..models.project import ProjectCreate, ProjectOut

class ProjectService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_project(self, project_in: ProjectCreate) -> ProjectOut:
        new_project = Project(
            title=project_in.title,
            description=project_in.description,
            start_date=project_in.start_date,
            end_date=project_in.end_date,
            pi_id=project_in.pi_id,
            budget=project_in.budget,
        )
        self.db.add(new_project)
        await self.db.commit()
        await self.db.refresh(new_project)
        return ProjectOut.from_orm(new_project)

    async def get_project(self, project_id: int) -> ProjectOut:
        result = await self.db.execute(select(Project).where(Project.id == project_id))
        project = result.scalar_one_or_none()
        if not project:
            raise NoResultFound(f"Project {project_id} not found")
        return ProjectOut.from_orm(project)

    async def list_projects(self):
        result = await self.db.execute(select(Project))
        projects = result.scalars().all()
        return [ProjectOut.from_orm(p) for p in projects]
