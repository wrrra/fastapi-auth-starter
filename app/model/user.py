from sqlalchemy import Column, String, Integer

from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String,nullable=False, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)