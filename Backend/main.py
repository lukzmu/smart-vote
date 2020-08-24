from fastapi import FastAPI
from blockchain.blockchain import Blockchain

# Start applications
app = FastAPI()
blockchain_app = Blockchain()

# Import API views
from urls import *