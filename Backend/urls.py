from main import app, blockchain_app

from schema import (
    BasicResponse,
    WalletResponse,
    Transaction,
    TransactionResponse,
    BlockchainValidationResponse,
)


@app.get('/', response_model=BasicResponse)
def ping_api_root():
    return {
        'message': 'Smart Vote API. Making voting smart 😅.'
    }

@app.get('/validate', response_model=BlockchainValidationResponse)
def validate_blockchain_instance():
    return {
        'is_valid': blockchain_app.validate_chain()
    }

@app.get('/wallet', response_model=WalletResponse)
def generate_wallet_keys():
    private_key, public_key = blockchain_app.generate_wallet()
    return {
        'private_key': private_key,
        'public_key': public_key,
    }

@app.post('/transaction', response_model=TransactionResponse)
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
