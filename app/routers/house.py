from app.auth.dependencies import get_current_user, get_db
from app.models.car import Car
from app.models.house import House
from app.models.garage import Garage
from app.models.user import User
from app.schemas.house import HouseCreate, HouseOut
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

import uuid

router = APIRouter(prefix="", tags=["Houses"])


@router.post("/", response_model=HouseOut)
def create_house(data: HouseCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    house = House(title=data.title, address=data.address)
    house.owners.append(user)
    db.add(house)
    db.commit()
    db.refresh(house)

    return HouseOut(
        id=getattr(house, "id"),
        title=getattr(house, "title"),
        address=getattr(house, "address"),
        owner_ids=[u.id for u in house.owners],
    )


@router.get("/", response_model=list[HouseOut])
def get_my_houses(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if getattr(user, "is_admin", False):
        houses = db.query(House).all()
    else:
        houses = db.query(House).filter(House.owners.any(id=user.id)).all()

    return [
        HouseOut(
            id=getattr(h, "id"),
            title=getattr(h, "title"),
            address=getattr(h, "address"),
            owner_ids=[u.id for u in h.owners],
        )
        for h in houses
    ]


@router.delete("/{house_id}")
def delete_house(house_id: UUID, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    house = db.query(House).filter(House.id == house_id).first()
    if not house:
        raise HTTPException(status_code=404, detail="House not found")

    # Permission check
    if user not in house.owners and not bool(user.is_admin):
        raise HTTPException(status_code=403, detail="Not allowed to delete this house")

    # Clear house_id for each garage in this house, and clear garage_id for cars in those garages
    garages = db.query(Garage).filter(Garage.house_id == house_id).all()
    for garage in garages:
        # Clear garage_id for each car in this garage
        cars = db.query(Car).filter(Car.garage_id == garage.id).all()
        for car in cars:
            car.garage_id = None
        garage.house_id = None

    db.delete(house)
    db.commit()
    return {"detail": "House deleted"}
