from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Dict
from app.schema.user import UserCreate, UserLogin

from app.service.database import get_db
from app.service import auth as auth_service

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

@router.post('/login')
def login(request: UserLogin, db: Session = Depends(get_db)):
    return auth_service.login(db, request)


@router.post('/register')
def register(request: UserCreate, db: Session = Depends(get_db)):
    return auth_service.register(db, request)


@router.post('/me')
def me():
    pass


@router.post('/refresh-token')
def refresh_token():
    pass

