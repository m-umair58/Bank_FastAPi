from fastapi import FastAPI
from database import engine
from router import user_router,account_router,transaction_router,login_router,loan_router,report_router
from models import account_model,transaction_model,user_model

# creating tables in database
account_model.Base.metadata.create_all(bind=engine)
user_model.Base.metadata.create_all(bind=engine)
transaction_model.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(login_router.router)
app.include_router(user_router.router)
app.include_router(account_router.router)
app.include_router(transaction_router.router)
app.include_router(loan_router.router)
app.include_router(report_router.router)