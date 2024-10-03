from models.transaction_model import Transaction
from sqlalchemy.orm import Session

class transaction_queries:
    def get_transaction_by_id(t_id,db:Session):
        return db.query(Transaction).filter(Transaction.transaction_id==t_id).first()

    def add_transaction(transaction,db:Session):
        db.add(transaction)
        db.commit()
