from typing import Dict
from sqlalchemy.orm.session import Session

from app.model import User


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: Dict):
    new_user = User(name=user.name,email=user.email,password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user