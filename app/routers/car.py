from app.auth.dependencies import get_current_user, get_db
from app.models.car import Car
from app.models.garage import Garage
from app.models.user import User
from app.schemas.car import CarCreate, CarOut
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import uuid

router = APIRouter(prefix="", tags=["Cars"])


def user_owns_garage_or_admin(user: User, garage: Garage):
    if bool(user.is_admin):
        return True
    house = garage.house
    return user in house.owners


@router.post("/", response_model=CarOut)
def create_car(data: CarCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    garage_id = None

    if data.garage_id:
        # Accept both UUID and str, convert str to UUID
        if isinstance(data.garage_id, uuid.UUID):
            garage_id = data.garage_id
        else:
            try:
                garage_id = uuid.UUID(data.garage_id)
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid garage_id format")
        garage = db.query(Garage).filter(Garage.id == garage_id).first()
        if not garage:
            raise HTTPException(status_code=404, detail="Garage not found")
        # Check: is the user an owner of the garage or admin
        if user not in garage.owners and not bool(user.is_admin):
            raise HTTPException(status_code=403, detail="Not allowed to add car to this garage")

    car = Car(model=data.model, garage_id=garage_id)
    car.owners.append(user)
    db.add(car)
    db.commit()
    db.refresh(car)
    return car


@router.get("/", response_model=List[CarOut])
def get_my_cars(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    cars = db.query(Car).filter(Car.owners.any(id=user.id)).all()
    return cars


@router.delete("/{car_id}")
def delete_car(car_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    try:
        car_uuid = uuid.UUID(car_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid car_id format")

    car = db.query(Car).filter(Car.id == car_uuid).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    # Check if user is owner or admin
    if user not in car.owners and not bool(user.is_admin):
        raise HTTPException(status_code=403, detail="Not allowed to delete this car")

    db.delete(car)
    db.commit()
    return {"detail": "Car deleted"}
