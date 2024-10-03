from db_queries.loan_queries import loan_queries
from fastapi import HTTPException
from starlette import status
from models.loan_model import Loan

class loan_service:
    def get_loan(loan_amount,days,user_data,db):
        loan_min=10000
        loan_max=1000000
        if loan_amount<loan_min and loan_amount>loan_max:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Loan should be within the range {loan_min}-{loan_max}")
        
        new_loan=Loan(
            amount=loan_amount,
            days = days,
            user_id=user_data['id']
        )
        loan_queries.add_loan(new_loan,db)
        return {"Details":"Loan granted successfully"}
    
    def get_loan_by_user_id(user_data,db):
        return loan_queries.get_loan_by_id(user_data['id'],db)
