from fastapi import FastAPI
from blockchain.blockchain import Blockchain
from fastapi_sqlalchemy import DBSessionMiddleware

# Start applications
app = FastAPI()
blockchain_app = Blockchain()

# Middleware
app.add_middleware(
    DBSessionMiddleware,
    db_url='postgresql+psycopg2://postgres:postgres@postgres:5432',
)

# Import API views
from urls import *