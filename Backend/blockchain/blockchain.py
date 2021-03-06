import uuid
import binascii

import Crypto
from Crypto.PublicKey import RSA

from blockchain.block import Block
from blockchain.transaction import Transaction


class Blockchain:
    def __init__(self):
        self.transactions = []
        self.chain = []
        self._create_genesis()

    def _create_genesis(self):
        self._add_block('00')

    def validate_chain(self):
        for index in range(1, len(self.chain)):
            last_block = self.chain[index - 1]
            block = self.chain[index]
            if block.previous_hash != last_block.get_hash():
                return False
        return True

    def _add_block(self, previous_hash):
        new_block = Block(
            block_number=len(self.chain) + 1,
            transactions=self.transactions,
            nonce=len(self.chain),
            previous_hash=previous_hash,
        )
        self.transactions = []
        self.chain.append(new_block)
        return new_block

    def add_transaction(self, sender, recipient, signature):
        transaction = Transaction(
            sender=sender,
            recipient=recipient,
            value=1,
            signature=signature,
        )

        self.transactions.append(transaction)

        # Automatically add blocks after transaction
        # only for hackathon presentation purposes.
        # New block after each transaction, change to
        # whatever you want or comment to make it valid.
        if len(self.transactions) == 1:
            self._add_block(self.chain[-1].get_hash())

        return len(self.chain) + 1
    
    def generate_wallet(self):
        gen = Crypto.Random.new().read
        private_key = RSA.generate(1024, gen)
        public_key = private_key.publickey()

        private_hex = binascii.hexlify(
            private_key.exportKey(format='DER'),
        ).decode('ascii')
        public_hex = binascii.hexlify(
            public_key.exportKey(format='DER'),
        ).decode('ascii')

        return private_hex, public_hex
    
    def get_voting_transactions(self, vote_recipients):
        result = {vr: 0 for vr in vote_recipients}

        for block in self.chain:
            for transaction in block.transactions:
                if transaction.recipient in result.keys():
                    result[transaction.recipient] += transaction.value

        return result
