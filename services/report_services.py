from schemas.account_schema import AccountCreate,AccountGet
from db_queries.report_queries import report_queries
# from fastapi import HTTPException
# from starlette import status
# from models.account_model import Account

class report_services:
    def transfered_money(user_data,db):
        return report_queries.transfered_money(user_data,db)
    
    def transfered_money_to(receiver_acc,user_data,db):
        return report_queries.transfered_money_to(receiver_acc,user_data,db)
    
    def received_money(user_data,db):
        return report_queries.received_money(user_data,db)
    
    def received_money_from(sender_acc,user_data,db):
        return report_queries.transfered_money_to(sender_acc,user_data,db)
    
    def deposits(user_data,db):
        return report_queries.deposits(user_data,db)
    
    def withdraw(user_data,db):
        return report_queries.withdraw(user_data,db)