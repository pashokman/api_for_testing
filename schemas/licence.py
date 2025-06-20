from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID


class DriverLicenceBase(BaseModel):
    licence_number: str = Field(..., min_length=1)


class DriverLicenceCreate(DriverLicenceBase):
    pass


class DriverLicenceOut(DriverLicenceBase):
    id: UUID
    user_id: UUID

    model_config = ConfigDict(from_attributes=True)
