from pydantic import BaseModel,EmailStr


class OurModelClass(BaseModel):
    class Config:
        from_attributes = True


class AccountCreate(OurModelClass):
    user_id:int
    acc_type:str
    acc_balance:int

class AccountGet(OurModelClass):
    acc_id:int
    acc_number:str
    user_id:int
    acc_type:str
    acc_balance:int

class AccountUpdate(OurModelClass):
    acc_id:int
    acc_type:str
    acc_balance:int
