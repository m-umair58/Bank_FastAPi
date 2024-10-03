from sqlalchemy import Column, Integer,String, Date
from sqlalchemy.orm import relationship
from datetime import date
from database import Base

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    user_email = Column(String, unique=True, nullable=False)
    user_password = Column(String, nullable=False)
    user_phone_number = Column(String, nullable=False)
    user_address = Column(String, nullable=True)
    user_role = Column(String,nullable=False)

    # Define the relationship with the Account model
    accounts = relationship("Account", back_populates="user")


