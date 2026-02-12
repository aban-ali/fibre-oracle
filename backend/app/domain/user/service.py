from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.domain.user.models import User
from app.domain.user.schema import UserCreate


async def get_user_by_email(db: AsyncSession, email: str) -> User | None:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().one_or_none()


async def create_user(db: AsyncSession, user_create: UserCreate) -> User:
    existing_user = await get_user_by_email(db, user_create.email)
    if existing_user:
        raise ValueError(f"User with email {user_create.email} already exists")
    
    user = User(
        email=user_create.email,
        password_hash=user_create.password,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user