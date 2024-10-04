from models.account_model import Account
from sqlalchemy.orm import Session

class account_queries:
    def get_account_by_acc_number(acc_num,db:Session):
        return db.query(Account).filter(Account.acc_number==acc_num).first()
    
    def get_account_by_acc_id(acc_id,db:Session):
        return db.query(Account).filter(Account.acc_id==acc_id).first()
    
    def get_account_by_user_id(user_id,db:Session):
        return db.query(Account).filter(Account.user_id==user_id).first()
    
    def get_account_by_id(account_id,db:Session):
        return db.query(Account).filter(Account.acc_id==account_id).first()
    
    def get_latest_account_number(db:Session):
        return db.query(Account).order_by(Account.acc_id.desc()).first()
    
    def match_acc_with_user(user_id,acc_id,db:Session):
        return db.query(Account).filter(
            Account.acc_id==acc_id,
            Account.user_id==user_id
        ).first()
    
    def add_acc(account,db:Session):
        db.add(account)
        db.commit()

    def delete_account(account,db:Session):
        db.delete(account)
        db.commit()

    def commit(db:Session):
        db.commit()