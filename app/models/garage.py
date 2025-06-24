from app.database.session import Base
from app.models.associations import garage_owners
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

import uuid


class Garage(Base):
    __tablename__ = "garages"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    house_id = Column(UUID(as_uuid=True), ForeignKey("houses.id"), nullable=True)

    house = relationship("House", back_populates="garages")
    owners = relationship("User", secondary=garage_owners, back_populates="owned_garages")
    cars = relationship("Car", back_populates="garage", cascade="all, delete-orphan")
