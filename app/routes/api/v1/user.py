from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/users", tags=["users"])

@router.post('/')
def create_user():
    pass

@router.get('/')
def list_users():
    pass

@router.get('/:id')
def get_user():
    pass

@router.put('/:id')
def update_user():
    pass

@router.delete('/')
def delete_user():
    pass