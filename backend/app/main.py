from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .app.api.project import router as project_router

DATABASE_URL = "postgresql+asyncpg://user:password@localhost:5432/research_db"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

app = FastAPI(title="Research Activity Support API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(project_router)

# Dependency
async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
