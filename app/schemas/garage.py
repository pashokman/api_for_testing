from app.schemas.user import UserOut
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from uuid import UUID


class GarageBase(BaseModel):
    title: str


class GarageCreate(GarageBase):
    house_id: Optional[UUID] = None


class GarageOut(GarageBase):
    id: UUID
    house_id: Optional[UUID] = None
    owners: List[UserOut]

    model_config = ConfigDict(from_attributes=True)
