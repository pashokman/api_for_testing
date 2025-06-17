from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

from schemas.user import UserOut


class CarBase(BaseModel):
    model: str
    garage_id: Optional[UUID] = None


class CarCreate(CarBase):
    pass


class CarOut(CarBase):
    id: UUID
    owners: List[UserOut]

    class Config:
        from_attributes = True
