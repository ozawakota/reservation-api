from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from .database import Base

# テーブル設計

class User(Base):
  __tablename__ = 'users'
  user_id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True)


class Room(Base):
  __tablename__ = 'rooms'