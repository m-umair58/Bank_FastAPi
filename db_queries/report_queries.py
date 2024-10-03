from models.transaction_model import Transaction
from models.account_model import Account
from db_queries.account_queries import account_queries
from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette import status

class report_queries:
    def transfered_money(user_data,db:Session):
        return db.query(Transaction).filter(
            Transaction.senders_acc_id==user_data['acc_id'],
            Transaction.transaction_type=="transfer"
            ).all()
    
    def transfered_money_to(receiver_acc,user_data,db:Session):
        return db.query(Transaction).filter(
            Transaction.receivers_acc_id==receiver_acc,
            Transaction.senders_acc_id==user_data['acc_id'],
            Transaction.transaction_type=="transfer"
            ).all()
    
    def received_money(user_data,db:Session):
        return db.query(Transaction).filter(
            Transaction.receivers_acc_id==user_data['acc_id'],
            Transaction.transaction_type=="transfer"
            ).all()
    
    def transfered_money_to(sender_acc,user_data,db:Session):
        return db.query(Transaction).filter(
            Transaction.senders_acc_id==sender_acc,
            Transaction.receivers_acc_id==user_data['acc_id'],
            Transaction.transaction_type=="transfer"
            ).all()
    
    def deposits(user_data,db:Session):
        return db.query(Transaction).filter(
            Transaction.senders_acc_id==user_data['acc_id'],
            Transaction.transaction_type=="deposit"
        ).all()

    def withdraw(user_data,db:Session):
        return db.query(Transaction).filter(
            Transaction.senders_acc_id==user_data['acc_id'],
            Transaction.transaction_type=="withdraw"
        ).all()