from app.schemas.user import UserOut
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from uuid import UUID


class CarBase(BaseModel):
    model: str
    garage_id: Optional[UUID] = None


class CarCreate(CarBase):
    pass


class CarOut(CarBase):
    id: UUID
    owners: List[UserOut]

    model_config = ConfigDict(from_attributes=True)
