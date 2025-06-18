from auth.auth_handler import get_password_hash
from auth.dependencies import get_current_user, get_db
from fastapi import APIRouter, Depends, HTTPException
from models.user import User
from schemas.user import UserCreate, UserOut
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    if user_data.username == "":
        raise HTTPException(status_code=400, detail="Username field is required")
    if user_data.password == "":
        raise HTTPException(status_code=400, detail="Password field is required")
    existing_username = db.query(User).filter(User.username == user_data.username).first()
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already taken")
    if user_data.email is not None:
        existing_email = db.query(User).filter(User.email == user_data.email).first()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=get_password_hash(user_data.password),
        is_admin=False,  # User can't create admin by itself
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user
