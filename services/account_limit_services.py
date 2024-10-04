from db_queries.account_limit_queries import account_limit_queries
from db_queries.user_queries import user_queries
from fastapi import HTTPException
from starlette import status
from models.account_limits_model import account_limit_model

class account_limit_services:
    def create_account_limit(account_type,daily_limit,monthly_limit,user_data,db):
        if daily_limit>=monthly_limit:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Monthly account limit should be greater than daily account limit!"
                )

        user_details=user_queries.get_user_by_id(user_data['id'],db)

        if user_details.user_role!="admin":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Only admin can create account_limit!")
        
        account_limit_details=account_limit_queries.get_account_limit_by_type(account_type,db)
        if account_limit_details is not None:
            if account_limit_details.account_type == account_type:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Account limit type already exists !")
        
        new_account_limit=account_limit_model(
            account_type = account_type,
            daily_limit = daily_limit,
            monthly_limit = monthly_limit
        )
        account_limit_queries.add_account_limit(new_account_limit,db)

        return {"Details":"New account type with its limits has been added"}
    
    def update_account_limit(account_type,daily_limit,monthly_limit,user_data,db):
        user_details=user_queries.get_user_by_id(user_data['id'],db)

        if user_details.user_role!="admin":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Only admin can create account_limit!")
        
        account_limit_details=account_limit_queries.get_account_limit_by_type(account_type,db)
        if account_limit_details is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Account limit type not found!")
        
        account_limit_details.daily_limit=daily_limit
        account_limit_details.monthly_limit=monthly_limit

        account_limit_queries.commit(db)

        return {"Details":"Account limits have been updated"}
    
    def delete_account_limit(account_type,user_data,db):
        user_details=user_queries.get_user_by_id(user_data['id'],db)

        if user_details.user_role!="admin":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Only admin can create account_limit!")
        
        account_limit_details=account_limit_queries.get_account_limit_by_type(account_type,db)
        if account_limit_details is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Account limit type not found!")
        
        account_limit_queries.delete(account_limit_details,db)

        return {"Details":"Account limit type has been deleted"}


