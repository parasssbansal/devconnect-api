from fastapi import APIRouter, Depends
from requests import post
from sqlalchemy.orm import Session
from models import post
from database.db import get_db
from models.post import Post
from schemas.post_schema import PostCreate

router = APIRouter()

@router.post("/create")
def create_post(post:PostCreate,db:Session=Depends(get_db)):
    new_post=Post(
        user_id=1,
        content=post.content
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"message":"Post created successfully"}

@router.get("/getallposts")
def get_all_posts(db:Session=Depends(get_db)):
    posts=db.query(Post).all()
    return posts

@router.get("/getpost/{user_id}")
def get_user(user_id:int,db:Session=Depends(get_db)):
    posts=db.query(Post).filter(Post.user_id==user_id).all()
    return posts

@router.delete("/deletepost/{id}")
def delete_post(id:int,db:Session=Depends(get_db)):
    post=db.query(Post).filter(Post.id==id).first()
    if not post:
        return {"message":"Post not found"}
    db.delete(post)
    db.commit()
    return {"message":"Post deleted successfully"}