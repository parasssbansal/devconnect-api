from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from models.user import User
from schemas.user_schema import UserCreate, UserLogin, UserResponse
from utils.hash import hash_password, verify_password
from utils.token import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        return {"error": "User not found"}
    if not verify_password(user.password, db_user.password):
        return {"error": "Invalid password"}
    token = create_access_token({"user_id": db_user.id})
    return {
        "access_token": token,
        "token_type": "bearer"
    }
