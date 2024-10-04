from db_queries.transaction_queries import transaction_queries
from schemas.account_schema import AccountGet
from db_queries.account_queries import account_queries
from db_queries.account_limit_queries import account_limit_queries
from fastapi import HTTPException
from starlette import status
from models.transaction_model import Transaction
from datetime import date

def total_transactions(transactions):
        total_amount=0
        for transaction in transactions:
            total_amount += transaction.amount

        return total_amount

class TransactionServices:
    
    def create_transaction(t_type,amount,receiver,user_data,db):
        if t_type=='deposit' or t_type=='withdraw' :
            if receiver:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="There Should be no receiver id here")

        if t_type=='transfer' and receiver<=0:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You need put a valid receiver account id!")
        if t_type=='transfer' and receiver is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You need put a valid receiver account id!")

        if user_data["acc_id"]==0:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You need to create an account first!")
        if user_data['acc_id']==receiver:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You cannot send money to the same account!")
        # above all are checks

        # check the account type
        account_details= account_queries.get_account_by_acc_id(user_data["acc_id"],db)
        account_limit_details = account_limit_queries.get_account_limit_by_type(account_details.acc_type,db)

        # to check daily transaction limit
        daily_transactions = transaction_queries.get_transaction_for_current_day(user_data['acc_id'],date.today(),db)

        daily_transaction_amount = total_transactions(daily_transactions)
        print("*********",daily_transaction_amount,"************")
        if account_limit_details.daily_limit<daily_transaction_amount+amount:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You have crossed your daily transaction limit!")

        monthly_transactions = transaction_queries.get_transactions_for_current_month(user_data['acc_id'],date.today(),db)
        monthly_transaction_amount = total_transactions(monthly_transactions)
        print("*********",monthly_transaction_amount,"************")

        if account_limit_details.monthly_limit<monthly_transaction_amount+amount:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You have crossed your monthly transaction limit!")

        account_id=account_queries.get_account_by_acc_id(user_data['acc_id'],db)
        if t_type=="deposit":
            get_acc:AccountGet=account_queries.get_account_by_acc_id(account_id.acc_id,db)
            get_acc.acc_balance+=amount
            account_queries.commit(db)
        elif t_type=="withdraw":
            get_acc:AccountGet=account_queries.get_account_by_acc_id(account_id.acc_id,db)
            if amount>50000:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You can only withdraw 50,000 each time")

            if amount>get_acc.acc_balance:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Insuficient Balance")
            get_acc.acc_balance-=amount
            account_queries.commit(db)
        elif t_type=="transfer":
            get_acc:AccountGet=account_queries.get_account_by_acc_id(account_id.acc_id,db)# senders decrement
            if amount>get_acc.acc_balance:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Sender has Insuficient Balance")
            get_acc.acc_balance-=amount
            account_queries.commit(db)

            get_acc2:AccountGet=account_queries.get_account_by_acc_id(receiver,db)# recievers increment
            if get_acc2 is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Receiver account not found!")

            get_acc2.acc_balance+=amount
            account_queries.commit(db)
            
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Please Select a correct Transaction type")
        
        new_transaction=Transaction(
            transaction_type = t_type,
            senders_acc_id = account_id.acc_id,
            receivers_acc_id = receiver,
            amount = amount
        )

        transaction_queries.add_transaction(new_transaction,db)

        return {"Details":"Transaction has been done!"}
