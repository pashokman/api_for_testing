from app.auth.auth_handler import get_password_hash
from app.config import ADMIN_PASSWORD
from app.database.session import engine, SessionLocal, Base
from app.models.car import Car
from app.models.garage import Garage
from app.models.house import House
from app.models.licence import DriverLicence
from app.models.user import User
from sqlalchemy.orm import Session


# Creating all tables
Base.metadata.create_all(bind=engine)

# Creating session
db: Session = SessionLocal()

# Checking if admin already exists
existing_admin = db.query(User).filter(User.username == "admin").first()
if not existing_admin:
    admin_user = User(
        username="admin",
        email="admin@example.com",
        hashed_password=get_password_hash(ADMIN_PASSWORD),
        is_admin=True,
    )
    db.add(admin_user)
    db.commit()
    print("Admin created")
else:
    print("ℹAdmin already exists")
