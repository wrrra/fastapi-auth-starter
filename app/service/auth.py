from fastapi import HTTPException, status

from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.model.user import User

from app.schema.user import UserCreate, UserLogin
from app.service.user import create_user, get_user_by_email


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def register(db: Session, user: UserCreate):
    check_user = get_user_by_email(db=db, email=user.email)
    
    if check_user:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Incorrect email or password")

    hashed_password = hash(user.password)

    user.password = hashed_password

    new_user = create_user(db,user)

    return {
        'status': 'success',
        'data': {
            'name': new_user.name,
            'email': new_user.email
        }
    }

def login(db: Session, user: UserLogin):
    check_user = get_user_by_email(db=db, email=user.email)

    if not check_user:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid email or password")
    
    check_login = verify(user.password,check_user.password)

    if not check_login:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid email or password")

    return {
        'status': 'success login',
        'data': {
            'name': check_user.name,
            'email': check_user.email
        }
    }