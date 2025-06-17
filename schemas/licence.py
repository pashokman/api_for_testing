from pydantic import BaseModel
from uuid import UUID


class DriverLicenceBase(BaseModel):
    licence_number: str


class DriverLicenceCreate(DriverLicenceBase):
    pass


class DriverLicenceOut(DriverLicenceBase):
    id: UUID
    user_id: UUID

    class Config:
        from_attributes = True
