from fastapi import APIRouter
# from schemas.transaction_schema import Create_Transaction
from services.transaction_services import TransactionServices
from oauth2 import get_user_info
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix='/transaction',tags=['Transaction'])

@router.post('/create')
def perform_transaction(t_type,amount:int,receiver:int|None=None,user_data=Depends(get_user_info),db:Session=Depends(get_db)):
    return TransactionServices.create_transaction(t_type,amount,receiver,user_data,db)