from schemas.transaction_schema import Create_Transaction
from db_queries.transaction_queries import transaction_queries
from schemas.account_schema import AccountCreate,AccountGet
from db_queries.account_queries import account_queries
from fastapi import HTTPException
from starlette import status
from models.transaction_model import Transaction
from fastapi import Depends
from oauth2 import get_user_info
from sqlalchemy.orm import Session
from database import get_db

class TransactionServices:
    def create_transaction(t_type,amount,receiver:int|None=None,user_data=Depends(get_user_info),db:Session=Depends(get_db)):
        if t_type=='deposit' or t_type=='withdraw' and receiver:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="There Should be no receiver id here")

        if t_type=='transfer' and receiver<=0:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You need put a valid receiver account id!")
        if t_type=='transfer' and receiver is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You need put a valid receiver account id!")

        if user_data['acc_id']==0:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You need to create an account first!")
        account_id=account_queries.get_account_by_acc_id(user_data['acc_id'],db)
        if user_data['acc_id']==receiver:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You cannot send money to the same account!")

        if t_type=="deposit":
            get_acc:AccountGet=account_queries.get_account_by_acc_id(account_id.acc_id,db)
            get_acc.acc_balance+=amount
            account_queries.commit(db)
        elif t_type=="withdraw":
            get_acc:AccountGet=account_queries.get_account_by_acc_id(account_id.acc_id,db)
            if amount>get_acc.acc_balance:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Insuficient Balance")
            get_acc.acc_balance-=amount
            account_queries.commit(db)
        elif t_type=="transfer":
            get_acc:AccountGet=account_queries.get_account_by_acc_id(account_id.acc_id,db)# senders decrement
            if amount>get_acc.acc_balance:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Sender has Insuficient Balance")
            get_acc.acc_balance-=amount
            account_queries.commit(db)

            get_acc2:AccountGet=account_queries.get_account_by_acc_id(receiver,db)# recievers increment
            if get_acc2 is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Receiver account not found!")

            get_acc2.acc_balance+=amount
            account_queries.commit(db)
            
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Please Select a correct Transaction type")
        
        new_transaction=Transaction(
            transaction_type = t_type,
            senders_acc_id = account_id.acc_id,
            receivers_acc_id = receiver,
            amount = amount
        )

        transaction_queries.add_transaction(new_transaction,db)

        return {"Details":"Transaction has been done!"}
