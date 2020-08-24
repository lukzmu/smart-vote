import uuid

from block import Block
from transaction import Transaction


MINE_SENDER = 'Smart Vote'
MINE_REWARD = 1
MINE_DIFF = 2


class Blockchain:
    def __init__(self):
        self.transactions = []
        self.chain = []
        self.nodes = set()
        self.node_id = str(uuid.uuid4()).replace('-', '')
        self._create_genesis()

    def _create_genesis(self):
        self.add_block(0, '00')

    def _validate_chain(self):
        for index in range(1, len(self.chain)):
            last_block = self.chain[index - 1]
            block = self.chain[index]
            if block.previous_hash != last_block.get_hash():
                return False
        return True

    def add_block(self, nonce, previous_hash):
        new_block = Block(
            block_number=len(self.chain) + 1,
            transactions=self.transactions,
            nonce=nonce,
            previous_hash=previous_hash,
        )
        self.transactions = []
        self.chain.append(new_block)
        return new_block

    def add_node(self, node_url):
        self.nodes.add(node_url)

    def add_transaction(self, sender, recipient, value, signature):
        transaction = Transaction(
            sender=sender,
            recipient=recipient,
            value=value,
            signature=signature,
        )

        if sender == MINE_SENDER or transaction.verify_signature():
            self.transactions.append(transaction)
            return len(self.chain) + 1
        return False
