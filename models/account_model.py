from sqlalchemy import Column, Integer,String, Date,ForeignKey
from sqlalchemy.orm import relationship
from datetime import date
from database import Base


class Account(Base):
    __tablename__ = 'accounts'
    
    acc_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    acc_number = Column(String, unique=True, nullable=False)
    acc_type = Column(String, nullable=False)
    acc_balance = Column(Integer, nullable=False)

    # Define the relationship with the User model
    user = relationship("User", back_populates="accounts")
    # Define the relationships with the Transaction model
    transactions_sent = relationship("Transaction", foreign_keys='Transaction.senders_acc_id', back_populates="sender_account")
    transactions_received = relationship("Transaction", foreign_keys='Transaction.receivers_acc_id', back_populates="receiver_account")

