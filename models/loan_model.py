from sqlalchemy import Column, Integer,String, Date
from database import Base
from datetime import datetime

class Loan(Base):
    __tablename__ = 'loan'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, nullable=False)
    date = Column(Date,  nullable=False, default=datetime.today)
    days = Column(Integer, nullable=False)
    return_date = Column(Date,nullable=True)
    user_id = Column(Integer,nullable=False)
