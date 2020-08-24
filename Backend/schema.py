import uuid
from pydantic import BaseModel
from typing import Optional, List


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

class Answer(BaseModel):
    id: Optional[uuid.UUID]
    description: str
    public_key: str
    private_key: str
    vote: Optional[uuid.UUID]

    class Config:
        orm_mode = True


class Vote(BaseModel):
    id: Optional[uuid.UUID]
    name: str
    category: str
    description: str
    image: str
    is_active: bool
    answers: List[Answer]

    class Config:
        orm_mode = True
