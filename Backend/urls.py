from typing import List
from fastapi_sqlalchemy import db
from main import app, blockchain_app
from schema import (
    BasicResponse,
    WalletResponse,
    Transaction,
    TransactionResponse,
    BlockchainValidationResponse,
    Vote,
    Answer,
)
from models import Vote as ModelVote
from models import Answer as ModelAnswer


@app.get('/', response_model=BasicResponse)
def ping_api_root():
    return {
        'message': 'Smart Vote API. Making voting smart 😅.'
    }

@app.get('/validate', response_model=BlockchainValidationResponse, tags=['blockchain'])
def validate_blockchain_instance():
    return {
        'is_valid': blockchain_app.validate_chain()
    }

@app.get('/wallet', response_model=WalletResponse, tags=['blockchain'])
def generate_wallet_keys():
    private_key, public_key = blockchain_app.generate_wallet()
    return {
        'private_key': private_key,
        'public_key': public_key,
    }

@app.post('/transaction', response_model=TransactionResponse, tags=['blockchain'])
def add_blockchain_transaction(transaction: Transaction):
    chain_length = blockchain_app.add_transaction(
        sender=transaction.sender,
        recipient=transaction.recipent,
        signature=transaction.signature,
    )
    return {
        'message': 'Vote completed!',
        'chain_length': chain_length,
    }


@app.post('/voting', response_model=Vote, tags=['database'])
def create_voting(vote: Vote):
    db_vote = ModelVote(
        name=vote.name,
        category=vote.category,
        description=vote.description,
        image=vote.image,
        is_active=vote.is_active,
    )
    db.session.add(db_vote)
    db.session.commit()
    db.session.refresh(db_vote)

    for answer in vote.answers:
        private_key, public_key = blockchain_app.generate_wallet()

        db_answer = ModelAnswer(
            description=answer.description,
            public_key=public_key,
            private_key=private_key,
            vote=str(db_vote.id),
        )
        db.session.add(db_answer)

    db.session.commit()
    return db_vote

@app.get('/voting', response_model=List[Vote], tags=['database'])
def get_all_active_votings():
    return [
        r for r in db.session.query(ModelVote).filter(
            ModelVote.is_active == True
        )
    ]
