from pydantic import BaseModel,EmailStr


class OurModelClass(BaseModel):
    class Config:
        from_attributes = True

class UserCreate(OurModelClass):
    name:str
    email:EmailStr
    password:str
    phone_number:str
    address:str

class UserOut(OurModelClass):
    id:int
    name:str

class UserShow(OurModelClass):
    name:str
    email:EmailStr
