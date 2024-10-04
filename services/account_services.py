from schemas.account_schema import AccountCreate,AccountGet
from db_queries.account_queries import account_queries
from db_queries.user_queries import user_queries
from fastapi import HTTPException
from starlette import status
from models.account_model import Account

class AccountServices:
    def get_account_by_id(user_data,db):
        return account_queries.get_account_by_acc_id(user_data['acc_id'],db)

    def create_account(account:AccountCreate,user_data,db):   
        user_details=user_queries.get_user_by_id(user_data['id'],db)
        if user_details.user_role != "admin":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Only admin has this previllege")
        if account.acc_type!="current" and account.acc_type!="saving":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Account should be current or saving!")

        account_number:AccountGet=account_queries.get_latest_account_number(db)
        def get_last_five_digits(account_number):
            # Ensure account_number is a string
            account_number_str = str(account_number)
            
            # Extract the last five digits
            last_five_digits = account_number_str[-5:]
            
            return int(last_five_digits)
        
        new_account_number=None
        if not account_number:
            new_account_number="PAK40200000"
        else:
            new_account_number = f"PAK402{get_last_five_digits(account_number.acc_number)+1:05d}"
        new_acc=Account(
            user_id = account.user_id,
            acc_number = new_account_number,
            acc_type = account.acc_type,
            acc_balance = account.acc_balance
        )

        account_queries.add_acc(new_acc,db)

        return {"details":"Account has been added successfully"}
    
    def update_account(account:AccountCreate,user_data,db):
        user_details=user_queries.get_user_by_id(user_data['id'],db)
        if user_details.user_role != "admin":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Only admin has this previllege")
        account_data= account_queries.get_account_by_user_id(account.user_id,db)
        if not account_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {account.user_id} doesn't exist!")
        
        account_data=account.model_dump()

        account_queries.commit(db)

        return {"details":"Changes has been made successfully!"}
    
    def delete_account(acc_id:int,user_data,db):
        user_details=user_queries.get_user_by_id(user_data['id'],db)
        if user_details.user_role != "admin":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Only admin has this previllege")
        account_data= account_queries.get_account_by_acc_id(acc_id,db)
        if not account_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Account with this id {acc_id} doesn't exists!")
        
        account_queries.delete_account(account_data,db)

        return {"Message":"Account has been deleted successfully"}