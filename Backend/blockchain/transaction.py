import binascii
import json
from collections import OrderedDict
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA


class Transaction:
    def __init__(self, sender, recipient, value, signature):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.signature = signature

    def verify_signature(self):
        public_key = RSA.importKey(
            binascii.unhexlify(self.sender),
        )
        verifier = PKCS1_v1_5.new(public_key)
        transaction_sha = SHA.new(
            json.dumps(self.to_dict()).encode('utf8'),
        )

        return verifier.verify(
            transaction_sha,
            binascii.unhexlify(self.signature),
        )

    def to_dict(self):
        return OrderedDict({
            'sender': self.sender,
            'recipient': self.recipient,
            'value': self.value,
        })
