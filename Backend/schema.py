import uuid
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


class Vote(BaseModel):
    id: uuid.UUID
    name: str
    category: str
    description: str
    image: str
    is_active: bool

    class Config:
        orm_mode = True

class Answer(BaseModel):
    id: uuid.UUID
    description: str
    public_key: str
    private_key: str
    vote: uuid.UUID

    class Config:
        orm_mode = True
