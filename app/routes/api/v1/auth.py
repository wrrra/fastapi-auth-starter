from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

@router.post('/login')
def login():
    pass


@router.post('/register')
def register():
    pass


@router.post('/me')
def me():
    pass


@router.post('/refresh-token')
def refresh_token():
    pass

