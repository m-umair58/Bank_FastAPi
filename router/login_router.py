from fastapi import APIRouter,Depends,HTTPException
from starlette import status
from services.login_services import login_services
from oauth2 import create_access_token
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.post('/token')
async def login(User_name,Password,Account_id:int,db:Session=Depends(get_db)):
    user_details=login_services.authenticate_user(User_name,Password,db)
    if Account_id<0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Account id should be greater than 0")
    elif Account_id==0:
        pass
    else:
        login_services.match_acc_with_user(user_details.id,Account_id,db)

    access_token = create_access_token(data={"user_id":user_details.id,"acc_id":Account_id})

    if user_details:
        return {"access_token":access_token,"token_type":"bearer"}