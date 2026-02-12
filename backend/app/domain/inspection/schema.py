import uuid
from datetime import datetime
from pydantic import BaseModel


class InspectionCreate(BaseModel):
    component_type: str


class InspectionRead(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    component_type: str
    created_at: datetime

    class Config:
        from_attributes = True
        str_strip_whitespace = True