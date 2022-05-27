from .database import Base
from sqlalchemy import Column, Integer


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False)