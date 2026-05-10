from fastapi import FastAPI
from .api import project as project_router

app = FastAPI(title="Research Activity Support API")

app.include_router(project_router)

# Simple startup event to create tables
from .database import engine, Base

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
