from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from models.follow import Follow
from schemas.follow_schema import FollowCreate

router=APIRouter()

@router.post("/follow/{user_id}")
def follow_user(user_id:int,follow=FollowCreate,db:Session=Depends(get_db)):
    new_follow=Follow(
        follower_id=1,
        following_id=user_id
    )
    db.add(new_follow)
    db.commit()
    db.refresh(new_follow)
    return {"message":"Followed successfully"}

@router.delete("/unfollow/{following_id}")
def unfollow(following_id:int,db:Session=Depends(get_db)):
    follow=db.query(Follow).filter(Follow.follower_id==1,Follow.following_id==following_id).first()
    if not follow:
        return {"message":"Follow relationship not found"}
    db.delete(follow)
    db.commit()
    return {"message":"Unfollowed successfully"}

@router.get("/followers/{user_id}")
def get_followers(user_id:int,db:Session=Depends(get_db)):
    followers=db.query(Follow).filter(Follow.following_id==user_id).all()
    return followers

@router.get("/following/{user_id}")
def get_following(user_id:int,db:Session=Depends(get_db)):
    following=db.query(Follow).filter(Follow.follower_id==user_id).all()
    return following
