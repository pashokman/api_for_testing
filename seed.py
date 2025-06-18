from auth.auth_handler import get_password_hash
from database.session import engine, SessionLocal, Base
from dotenv import load_dotenv
from models.car import Car
from models.garage import Garage
from models.house import House
from models.licence import DriverLicence
from models.user import User
from sqlalchemy.orm import Session

import os

load_dotenv()

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

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
    print("✅ Admin created")
else:
    print("ℹ️ Admin already exists")
