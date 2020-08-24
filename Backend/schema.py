from pydantic import BaseModel


class BasicResponse(BaseModel):
    message: str


class WalletResponse(BaseModel):
    private_key: str
    public_key: str


class Transaction(BaseModel):
    sender: str
    recipent: str
    signature: str


class TransactionResponse(BaseModel):
    message: str
    chain_length: int


class BlockchainValidationResponse(BaseModel):
    is_valid: bool
