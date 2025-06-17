import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from schemas.garage import GarageCreate, GarageOut
from models.garage import Garage
from models.house import House
from models.user import User
from models.car import Car
from auth.dependencies import get_current_user, get_db

router = APIRouter(prefix="", tags=["Garages"])


@router.post("/", response_model=GarageOut)
def create_garage(data: GarageCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    house_id = None
    if data.house_id:
        # Accept both UUID and str, convert str to UUID
        if isinstance(data.house_id, uuid.UUID):
            house_id = data.house_id
        else:
            try:
                house_id = uuid.UUID(data.house_id)
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid house_id format")
        house = db.query(House).filter(House.id == house_id).first()
        if not house:
            raise HTTPException(status_code=404, detail="House not found")
        # Check: is the user an owner of the house or admin
        if user not in house.owners and not bool(user.is_admin):
            raise HTTPException(status_code=403, detail="Not allowed to add garage to this house")

    new_garage = Garage(title=data.title, house_id=house_id)
    new_garage.owners.append(user)
    db.add(new_garage)
    db.commit()
    db.refresh(new_garage)
    return new_garage


@router.get("/", response_model=list[GarageOut])
def get_my_garages(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    garages = db.query(Garage).filter(Garage.owners.any(id=user.id)).all()
    return garages


@router.delete("/{garage_id}")
def delete_garage(garage_id: UUID, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    garage = db.query(Garage).filter(Garage.id == garage_id).first()
    if not garage:
        raise HTTPException(status_code=404, detail="Garage not found")

    if garage.house:
        if user not in garage.house.owners and not bool(user.is_admin):
            raise HTTPException(status_code=403, detail="Not allowed to delete this garage")
    else:
        if user not in garage.owners and not bool(user.is_admin):
            raise HTTPException(status_code=403, detail="Not allowed to delete this garage")

    # Clear field garage_id for each car that was in this garage
    cars = db.query(Car).filter(Car.garage_id == garage.id).all()
    for car in cars:
        car.garage_id = None

    db.delete(garage)
    db.commit()
    return {"detail": "Garage deleted"}
