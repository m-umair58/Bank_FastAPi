from models.transaction_model import Transaction
from sqlalchemy.orm import Session
from sqlalchemy import or_,func
from datetime import date

class transaction_queries:
    def get_transaction_by_id(t_id,db:Session):
        return db.query(Transaction).filter(Transaction.transaction_id==t_id).first()

    def add_transaction(transaction,db:Session):
        db.add(transaction)
        db.commit()

    def get_transaction_by_user_id(user_id, date_today, db: Session):
        return db.query(Transaction).filter(
            or_(
                Transaction.senders_acc_id == user_id,
                Transaction.receivers_acc_id == user_id
            ),
            func.date(Transaction.date) == date_today
        ).all()
