from models.account_limits_model import account_limit_model
from sqlalchemy.orm import Session

class account_limit_queries:
    def add_account_limit(new_account_limit,db:Session):
        db.add(new_account_limit)
        db.commit()

    def commit(new_account_limit,db:Session):
        db.commit()

    def get_account_limit_by_type(account_type,db:Session):
        return db.query(account_limit_model).filter(account_limit_model.account_type==account_type).first()
    
    def delete(account_limit,db:Session):
        db.delete(account_limit)