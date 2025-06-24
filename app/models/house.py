from app.database.session import Base
from app.models.associations import house_owners
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

import uuid


class House(Base):
    __tablename__ = "houses"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    address = Column(String, nullable=False)

    owners = relationship("User", secondary=house_owners, back_populates="owned_houses")
    garages = relationship("Garage", cascade="all, delete", back_populates="house")
