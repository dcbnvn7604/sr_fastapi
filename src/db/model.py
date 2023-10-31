from sqlalchemy import Column, Integer, String

from db.database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(30), unique=True, index=True)
    password = Column(String(60))
