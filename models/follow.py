from sqlalchemy import Column, Integer, String
from database.db import Base
class Follow(Base):
    __tablename__ = "follows"
    id = Column(Integer, primary_key=True, index=True)
    follower_id = Column(Integer)
    following_id = Column(Integer)