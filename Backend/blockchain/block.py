import time
import hashlib
import json
from collections import OrderedDict


class Block:
    def __init__(
        self,
        block_number,
        transactions,
        nonce,
        previous_hash,
    ):
        self.block_number = block_number
        self.timestamp = time.time()
        self.transactions = transactions
        self.nonce = nonce
        self.previous_hash = previous_hash

    def to_dict(self):
        return OrderedDict({
            'block_number': self.block_number,
            'nonce': self.nonce,
            'previous_hash': self.previous_hash,
        })

    def get_hash(self):
        return hashlib.sha256(
            json.dumps(self.to_dict()).encode('utf-8'),
        ).hexdigest()
