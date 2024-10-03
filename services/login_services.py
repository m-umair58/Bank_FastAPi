from db_queries.user_queries import user_queries
from fastapi import HTTPException
from schemas.user_schema import UserCreate,UserOut
from services.user_services import verify_password
from fastapi.security import OAuth2PasswordRequestForm

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

