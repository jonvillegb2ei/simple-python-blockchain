import json
import random
import string
import hashlib
from entry import Entry


class Block:

    def __init__(self, previous_hash: str, difficulty: int, entries=None, nonce: str = None, size: int = 10):
        self.previous_hash = previous_hash
        self.difficulty = difficulty
        self.entries = [] if entries is None else entries
        self.nonce = nonce
        self.size = size
        self.hash = None

    def __str__(self):
        return json.dumps({
            'previous_hash': self.previous_hash,
            'difficulty': self.difficulty,
            'entries': [str(entry) for entry in self.entries],
            'nonce': self.nonce,
            'size': self.size
        })

    def is_full(self):
        return len(self.entries) >= self.size

    def add_entry(self, entry: Entry):
        if self.is_full():
            return False
        self.entries.append(entry)
        return True

    @staticmethod
    def from_array(data: dict, entry_type=Entry):
        entries = [entry_type.from_array(json.loads(entry)) for entry in data['entries']]
        return Block(data['previous_hash'], data['difficulty'], entries, data['nonce'], data['size'])

    def get_hash(self):
        m = hashlib.sha256()
        m.update(str(self).encode())
        return m.hexdigest()

    def mine(self):
        if self.nonce is None:
            self.nonce = ''.join(random.choice(string.ascii_letters) for _ in range(32))
        while True:
            self.hash = self.get_hash()
            if self.hash[:self.difficulty] == "0" * self.difficulty:
                return self.hash
            else:
                self.nonce = ''.join(random.choice(string.ascii_letters) for _ in range(32))

    def get_entry_count(self):
        return len(self.entries)
