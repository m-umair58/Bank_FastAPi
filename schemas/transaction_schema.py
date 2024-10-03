from pydantic import BaseModel,EmailStr
from datetime  import datetime

class OurModelClass(BaseModel):
    class Config:
        from_attributes = True

class Create_Transaction(OurModelClass):
    type:str
    sender_acc_id:int
    receiver_acc_id:int|None = None
    amount:int