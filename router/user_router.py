from fastapi import APIRouter
from schemas.user_schema import UserCreate
from services.user_services import UserServices
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix='/user',tags=['User'])

@router.get('/{user_id}')
async def get_user_by_id(user_id,db:Session = Depends(get_db)):
    return UserServices.get_user_by_id(user_id,db)

@router.post('/create')
async def create_user(user:UserCreate,db:Session = Depends(get_db)):
    return UserServices.create_user(user,db)

@router.put('/update')
async def update_user(user:UserCreate,db:Session = Depends(get_db)):
    return UserServices.update_user(user,db)

@router.delete('/delete')
async def create_user(user:UserCreate,db:Session = Depends(get_db)):
    return UserServices.delete_user(user,db)
