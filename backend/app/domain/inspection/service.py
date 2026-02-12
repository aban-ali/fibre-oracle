import os
import uuid
import aiofiles

from backend.app.api.routers import inspection
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import UploadFile

from app.domain.models import Inspection, Image
from app.domain.schema import InspectionCreate

IMAGE_UPLOAD_DIR = "data/uploads/"

async def create_inspection(
    db: AsyncSession,
    user_id,
    inspection_create: InspectionCreate,  
) -> Inspection:
    inspection = Inspection(
        user_id=user_id,
        component_type=inspection_create.component_type
    )
    db.add(inspection)
    await db.commit()
    await db.refresh(inspection)
    return inspection

async def add_image_to_inspection(
    db: AsyncSession,
    inspection_id,
    image_file: UploadFile
) -> Image:
    stmt = select(Inspection).where(Inspection.id == inspection_id)
    result = await db.execute(stmt)
    inspection = result.scalar_one_or_none()
    if not inspection:
        raise ValueError("Inspection not found")

    os.makedirs(IMAGE_UPLOAD_DIR, exist_ok=True)

    file_extension = image_file.filename.split(".")[-1]
    new_filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = os.path.join(IMAGE_UPLOAD_DIR, new_filename)

    async with aiofiles.open(file_path, "wb") as out_file:
        out_file.write(await image_file.read())

    image = Image(
        inspection_id=inspection_id,
        file_path=file_path,
    )
    db.add(image)
    await db.commit()
    await db.refresh(image)
    return image    