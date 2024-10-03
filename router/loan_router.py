from fastapi import APIRouter
# from schemas.account_schema import AccountCreate
from services.loan_services import loan_service
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from oauth2 import get_user_info

router = APIRouter(prefix='/loan',tags=['Loan'])

@router.post('/get')
def get_loan(loan_amount:int,days:int,user_data=Depends(get_user_info),db:Session=Depends(get_db)):
    return loan_service.get_loan(loan_amount,days,user_data,db)

@router.get('/get')
def get_loan_by_user_id(user_data=Depends(get_user_info),db:Session=Depends(get_db)):
    return loan_service.get_loan_by_user_id(user_data,db)