from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from typing import Optional
import uuid

from database.session import Base


class Car(Base):
    __tablename__ = "cars"

    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid.uuid4())
    model = Column(String, nullable=False)
    garage_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), ForeignKey("garages.id"), nullable=True)

    garage = relationship("Garage", back_populates="cars")
    owners = relationship("User", secondary="car_owners", back_populates="cars")
