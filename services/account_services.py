from schemas.account_schema import AccountCreate,AccountGet
from db_queries.account_queries import account_queries
from fastapi import HTTPException
from starlette import status
from models.account_model import Account

class AccountServices:
    def get_account_by_id(user_data,db):
        return account_queries.get_account_by_user_id(user_data['id'],db)

    def create_account(account:AccountCreate,db):        
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
    
    def update_account(account:AccountCreate,db):
        account_data= account_queries.get_account_by_user_id(account.user_id,db)
        if not account_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {account.user_id} doesn't exist!")
        
        account_data=account.model_dump()

        account_queries.commit(db)

        return {"details":"Changes has been made successfully!"}
    
    def delete_account(account:AccountCreate,db):
        account_data= account_queries.get_account_by_user_id(account.user_id,db)
        if not account_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with this id {account.user_id} doesn't exists!")
        
        account_queries.delete_account(account_data,db)

        return {"Message":"Account has been deleted successfully"}