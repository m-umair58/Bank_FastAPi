from fastapi import APIRouter
# from schemas.transaction_schema import Create_Transaction
from services.report_services import report_services
from oauth2 import get_user_info
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db


router = APIRouter(prefix='/report',tags=['Reports and Analytics'])

@router.get('/all_transfers')
async def transfered_money(user_data=Depends(get_user_info),db:Session=Depends(get_db)):
    return report_services.transfered_money(user_data,db)

@router.get('/transfers_to')
async def transfered_money(receiver_acc:int,user_data=Depends(get_user_info),db:Session=Depends(get_db)):
    return report_services.transfered_money_to(receiver_acc,user_data,db)

@router.get('/all_received')
async def received_money(user_data=Depends(get_user_info),db:Session=Depends(get_db)):
    return report_services.received_money(user_data,db)

@router.get('/received_from')
async def received_money_from(sender_acc:int,user_data=Depends(get_user_info),db:Session=Depends(get_db)):
    return report_services.received_money_from(sender_acc,user_data,db)

@router.get('/deposits')
async def deposits(user_data=Depends(get_user_info),db:Session=Depends(get_db)):
    return report_services.deposits(user_data,db)

@router.get('/withdraw')
async def withdraw(user_data=Depends(get_user_info),db:Session=Depends(get_db)):
    return report_services.withdraw(user_data,db)