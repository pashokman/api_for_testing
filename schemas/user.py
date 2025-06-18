from pydantic import BaseModel, EmailStr, field_validator, ConfigDict
from typing import Optional
from uuid import UUID


class UserBase(BaseModel):
    username: str
    email: Optional[EmailStr] = None


class UserCreate(UserBase):
    password: str

    @field_validator("email", mode="before")
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v


class UserLogin(BaseModel):
    username: str
    password: str


class UserOut(UserBase):
    id: UUID
    is_admin: bool

    model_config = ConfigDict(from_attributes=True)
