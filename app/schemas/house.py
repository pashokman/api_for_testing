from pydantic import BaseModel, Field, ConfigDict
from typing import List
from uuid import UUID


class HouseBase(BaseModel):
    title: str
    address: str


class HouseCreate(HouseBase):
    pass  # did not accept owner_ids - it adding automaticaly from current_user


class HouseOut(HouseBase):
    id: UUID
    owner_ids: List[UUID] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)
