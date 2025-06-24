from app.auth.dependencies import get_current_user, get_db
from app.models.house import House
from app.models.user import User
from app.schemas.house import HouseCreate, HouseOut
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

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
def delete_house(house_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    house = db.query(House).filter(House.id == uuid.UUID(house_id)).first()
    if not house:
        raise HTTPException(status_code=404, detail="House not found")

    if user not in house.owners and not bool(user.is_admin):
        raise HTTPException(status_code=403, detail="Not your house")

    db.delete(house)
    db.commit()
    return {"detail": "House deleted"}
