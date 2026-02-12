from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models import Inspection
from app.domain.schema import InspectionCreate

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