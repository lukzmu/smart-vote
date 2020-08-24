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
    
    def __getattr__(self, attr):
        return self.data[attr]

    def sign_transaction(self):
        private_key = RSA.importKey(
            binascii.unhexlify(self.signature),
        )
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(self.to_dict()).encode('UTF-8')
        return binascii.hexlify(signer.sign(h)).decode('ascii')

    def to_dict(self):
        return OrderedDict({
            'sender': self.sender,
            'recipient': self.recipient,
            'value': self.value,
        })
