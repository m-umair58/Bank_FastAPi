from sqlalchemy import Column, Integer,String
from database import Base

class account_limit_model(Base):
    __tablename__ = 'account_limits' 
    
    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    account_type = Column(String,nullable=False,unique=True)
    daily_limit = Column(Integer,nullable=False)
    monthly_limit = Column(Integer,nullable=False)