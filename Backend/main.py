from fastapi import FastAPI
from blockchain.blockchain import Blockchain
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.middleware.cors import CORSMiddleware

# Start applications
app = FastAPI(
    title='Smart Vote API',
    description='Our awesome application for the Wizja Rozwoju hackathon 2020. Be sure to check out the repo: https://gitlab.com/lukzmu/smart-vote.',
    version='hacky alpha',
)
blockchain_app = Blockchain()

# Middleware
app.add_middleware(
    DBSessionMiddleware,
    db_url='postgresql+psycopg2://postgres:postgres@postgres:5432',
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import API views
from urls import *