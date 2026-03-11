from fastapi import FastAPI
from database.db import engine, Base
from routers import auth , posts , follow, users

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(follow.router)
app.include_router(users.router)
@app.get("/")
def read_root():
    return {"message": "Welcome to Devloper Connect API"}