import uuid

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import DBSessionDep

from app.domain.inspection.schema import InspectionCreate, InspectionRead
from app.domain.inspection.service import create_inspection

router = APIRouter(prefix="/inspections", tags=["inspections"])

@router.post(
    "",
    response_model=InspectionRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_new_inspection(
    inspection_create: InspectionCreate,
    db: AsyncSession = Depends(DBSessionDep),
):
    fake_user_id = uuid.UUID("13297c91-9684-4ec8-8294-adb3ba0e75f7")
    try:
        inspection = await create_inspection(db, user_id=fake_user_id, inspection_create=inspection_create)
        return inspection
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))