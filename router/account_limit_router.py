from fastapi import APIRouter
from services.account_limit_services import account_limit_services
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from oauth2 import get_user_info

router = APIRouter(prefix='/account_limit',tags=['Account-Limit'])

@router.post('/create')
async def create(account_type,daily_limit:int,monthly_limit:int,user_data=Depends(get_user_info),db:Session=Depends(get_db)):
    return account_limit_services.create_account_limit(account_type,daily_limit,monthly_limit,user_data,db)

@router.post('/update')
async def update(account_type,daily_limit:int,monthly_limit:int,user_data=Depends(get_user_info),db:Session=Depends(get_db)):
    return account_limit_services.update_account_limit(account_type,daily_limit,monthly_limit,user_data,db)

@router.post('/delete')
async def delete(account_type,user_data=Depends(get_user_info),db:Session=Depends(get_db)):
    return account_limit_services.delete_account_limit(account_type,user_data,db)