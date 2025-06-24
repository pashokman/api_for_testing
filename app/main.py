from app.auth.auth_router import router as auth_router
from app.database.session import engine, Base
from app.routers import user, house, garage, car, licence
from fastapi import FastAPI

app = FastAPI(title="Complete API for testing")

# Creating tables (using Alembic and production)
Base.metadata.create_all(bind=engine)

# Auth
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

# Main resources
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(house.router, prefix="/houses", tags=["Houses"])
app.include_router(garage.router, prefix="/garages", tags=["Garages"])
app.include_router(car.router, prefix="/cars", tags=["Cars"])
app.include_router(licence.router, prefix="/licences", tags=["Driver Licence"])
