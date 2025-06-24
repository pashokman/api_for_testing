from app.database.session import Base
from sqlalchemy import Column, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

import uuid


class DriverLicence(Base):
    __tablename__ = "driver_licences"
    __table_args__ = (UniqueConstraint("user_id", name="unique_user_licence"),)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    licence_number = Column(String, unique=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="driver_licence")
