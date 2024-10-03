from schemas.user_schema import UserCreate,UserShow
from db_queries.user_queries import user_queries
from fastapi import HTTPException
from starlette import status
from models.user_model import User
from passlib.context import CryptContext

bcrypt_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
def get_password_hash(password):
    return bcrypt_context.hash(password)

def verify_password(plain_password,hashed_password):
    return bcrypt_context.verify(plain_password,hashed_password)

class UserServices:
    def get_user_by_id(user_id,db):
        return user_queries.get_user_by_id(user_id,db)

    def create_user(user:UserCreate,db):
        user_data= user_queries.get_user_by_email(user.email,db)
        if user_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with this email already exists!")
        
        new_user = User(
            user_name = user.name,
            user_email =  user.email,
            user_password =get_password_hash(user.password),
            user_phone_number = user.phone_number,
            user_address = user.address
        )

        user_queries.add_user(new_user,db)
        return_user=UserShow(
            name=user.name,
            email=user.email
        )
        return return_user
    
    def update_user(user:UserCreate,db):
        user_data= user_queries.get_user_by_email(user.email,db)
        if not user_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with this email doesn't exists!")
        
        new_user = User(
            name = user.name,
            email =  user.email,
            password =get_password_hash(user.password),
            phone_number = user.phone_number,
            address = user.address
        )

        user_queries.add_user(new_user)

        return new_user
    
    def delete_user(user:UserCreate,db):
        user_data= user_queries.get_user_by_email(user.email,db)
        if not user_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with this email doesn't exists!")
        
        user_queries.delete_user(user_data,db)

        return {"Message":"User has been deleted successfully"}