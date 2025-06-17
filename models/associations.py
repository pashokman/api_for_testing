from sqlalchemy import UUID, Table, Column, ForeignKey
from database.session import Base


house_owners = Table(
    "house_owners",
    Base.metadata,
    Column("house_id", UUID(as_uuid=True), ForeignKey("houses.id"), primary_key=True),
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True),
)

garage_owners = Table(
    "garage_owners",
    Base.metadata,
    Column("garage_id", UUID(as_uuid=True), ForeignKey("garages.id"), primary_key=True),
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True),
)

car_owners = Table(
    "car_owners",
    Base.metadata,
    Column("car_id", UUID(as_uuid=True), ForeignKey("cars.id"), primary_key=True),
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True),
)
