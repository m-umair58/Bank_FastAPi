from fastapi import APIRouter
from schemas.account_schema import AccountCreate,AccountUpdate
from services.account_services import AccountServices
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from oauth2 import get_user_info

router = APIRouter(prefix='/account',tags=['Account'])

@router.get('')
async def get_account_by_id(user_data=Depends(get_user_info),db:Session = Depends(get_db)):
    return AccountServices.get_account_by_id(user_data,db)

@router.post('/create')
async def create_account(account:AccountCreate,user_data=Depends(get_user_info),db:Session = Depends(get_db)):
    return AccountServices.create_account(account,user_data,db)

@router.put('/update')
async def update_account(account:AccountUpdate,user_data=Depends(get_user_info),db:Session = Depends(get_db)):
    return AccountServices.update_account(account,db)

@router.delete('/delete')
async def delete_account(acc_id,user_data=Depends(get_user_info),db:Session = Depends(get_db)):
    return AccountServices.delete_account(acc_id,user_data,db)
