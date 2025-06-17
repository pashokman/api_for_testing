from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from models.associations import garage_owners, house_owners, car_owners

import uuid

from database.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4())
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

    driver_licence = relationship("DriverLicence", back_populates="user", uselist=False)
    owned_houses = relationship("House", secondary=house_owners, back_populates="owners")
    owned_garages = relationship("Garage", secondary=garage_owners, back_populates="owners")
    cars = relationship("Car", secondary=car_owners, back_populates="owners")
