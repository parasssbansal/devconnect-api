from fastapi import FastAPI , APIRouter, Depends
from database.db import engine, Base
from routers import auth , posts , follow
from sqlalchemy.orm import Session
from models import user
from database.db import get_db
from models.user import User
from schemas.user_schema import UserResponse

router=APIRouter()

@router.get("/users",response_model=list[UserResponse])
def get_users(db:Session=Depends(get_db)):
    users=db.query(User).all()
    return users

@router.patch("/changebio/{user_id}")
def change_bio(user_id:int , bio:str,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()
    if not user:
        return {"message":"User not found"}
    user.bio=bio
    db.commit()
    db.refresh(user)
    return {"message":"Bio updated successfully"}

@router.get("/user/{user_id}",response_model=UserResponse)
def get_single_user(user_id:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()
    if not user :
        return {"message":"User not found"}
    return user


