from models.user_model import User
from sqlalchemy.orm import Session

class user_queries:
    def get_user_by_id(user_id,db:Session):
        return db.query(User).filter(User.user_id==user_id).first()
    
    def get_user_by_email(user_email,db:Session):
        return db.query(User).filter(User.user_email==user_email).first()
    
    def get_userName(user_name,db:Session):
        return db.query(User).filter(User.user_name==user_name).first()
    
    def add_user(user,db:Session):
        db.add(user)
        db.commit()

    def delete_user(user,db:Session):
        db.delete(user)
        db.commit()