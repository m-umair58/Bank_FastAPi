from models.loan_model import Loan
from sqlalchemy.orm import Session

class loan_queries:
    def get_loan_by_id(user_id,db:Session):
        return db.query(Loan).filter(Loan.user_id==user_id).first()
    
    def add_loan(loan,db:Session):
        db.add(loan)
        db.commit()