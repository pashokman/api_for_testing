from pydantic import BaseModel, ConfigDict
from uuid import UUID


class DriverLicenceBase(BaseModel):
    licence_number: str


class DriverLicenceCreate(DriverLicenceBase):
    pass


class DriverLicenceOut(DriverLicenceBase):
    id: UUID
    user_id: UUID

    model_config = ConfigDict(from_attributes=True)
