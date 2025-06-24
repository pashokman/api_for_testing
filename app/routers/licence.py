from app.auth.dependencies import get_current_user, get_db
from app.models.licence import DriverLicence
from app.models.user import User
from app.schemas.licence import DriverLicenceCreate, DriverLicenceOut
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="", tags=["Driver Licence"])


@router.post("/", response_model=DriverLicenceOut)
def create_driver_licence(
    data: DriverLicenceCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)
):
    existing_licence = db.query(DriverLicence).filter(DriverLicence.user_id == user.id).first()
    if existing_licence:
        raise HTTPException(status_code=400, detail="User already has a driver licence")

    licence = DriverLicence(licence_number=data.licence_number, user_id=user.id)
    db.add(licence)
    db.commit()
    db.refresh(licence)
    return licence


@router.get("/", response_model=DriverLicenceOut)
def get_my_driver_licence(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    licence = db.query(DriverLicence).filter(DriverLicence.user_id == user.id).first()
    if not licence:
        raise HTTPException(status_code=404, detail="Driver licence not found")
    return licence


@router.delete("/")
def delete_my_driver_licence(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    licence = db.query(DriverLicence).filter(DriverLicence.user_id == user.id).first()
    if not licence:
        raise HTTPException(status_code=404, detail="Driver licence not found")

    db.delete(licence)
    db.commit()
    return {"detail": "Driver licence deleted"}
