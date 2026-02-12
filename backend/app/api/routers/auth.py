from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import DBSessionDep
from app.domain.user.schema import UserCreate, UserRead
from app.domain.user.service import create_user


router = APIRouter(prefix="/users", tags=["users"])

@router.post(
    "",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    user_create: UserCreate,
    db: AsyncSession = Depends(DBSessionDep),
):
    try:
        user = await create_user(db, user_create)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) 