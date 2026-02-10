from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.api.deps import DBSessionDep

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/db")
async def db_health(db: AsyncSession = Depends(DBSessionDep)):
    await db.execute(text("SELECT 1"))
    return {"database": "ok"}
