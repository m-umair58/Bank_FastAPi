from sqlalchemy import Column, Integer,String, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Transaction(Base):
    __tablename__ = 'transactions'
    
    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_type = Column(String, nullable=False)
    senders_acc_id = Column(Integer, ForeignKey('accounts.acc_id'), nullable=False)
    receivers_acc_id = Column(Integer, ForeignKey('accounts.acc_id'), nullable=True)
    date = Column(DateTime, nullable=False, default=datetime.today)
    amount = Column(Integer, nullable=False)

    # Define the relationships with the Account model
    sender_account = relationship("Account", foreign_keys=[senders_acc_id], back_populates="transactions_sent")
    receiver_account = relationship("Account", foreign_keys=[receivers_acc_id], back_populates="transactions_received")
