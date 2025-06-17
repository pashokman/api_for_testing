from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional

from schemas.user import UserOut


class GarageBase(BaseModel):
    title: str


class GarageCreate(GarageBase):
    house_id: Optional[UUID] = None


class GarageOut(GarageBase):
    id: UUID
    house_id: Optional[UUID] = None
    owners: List[UserOut]

    class Config:
        from_attributes = True
