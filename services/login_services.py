from db_queries.user_queries import user_queries
from fastapi import HTTPException
from schemas.user_schema import UserCreate,UserOut
from services.user_services import verify_password
from db_queries.account_queries import account_queries
from starlette import status

class login_services:
    def authenticate_user(User_name,Password,db):
        user_details=user_queries.get_userName(User_name,db)

        if user_details is None:
            raise HTTPException(status_code=404,detail="Email is Incorrect")
        
        if not verify_password(Password,user_details.user_password):
            raise HTTPException(status_code=404,detail="Password is Incorrect")
        
        user_show=UserOut(
            id=user_details.user_id,
            name=user_details.user_name
        )
        return user_show

    def match_acc_with_user(user_id,acc_id,db):
        acc_details = account_queries.match_acc_with_user(user_id,acc_id,db)
        if acc_details is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Account with id {acc_id} doesn't belong to the user with id {user_id}!"
                )

