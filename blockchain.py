from block import Block
from entry import Entry

import json


class Blockchain:

    origin_hash = '0000000000000000000000000000000000000000000000000000000000000000'

    def __init__(self, difficulty: int, block_size: int = 10, blocks: list = None):
        self.difficulty = difficulty
        self.block_size = block_size
        self.blocks = [Block(Blockchain.origin_hash, self.difficulty, None, None, block_size)] if blocks is None else blocks

    def add_entry(self, entry: Entry):
        if self.blocks[-1].is_full():
            hash = self.blocks[-1].mine()
            self.blocks.append(Block(hash, self.difficulty, None, None, self.block_size))
        self.blocks[-1].add_entry(entry)

    def __str__(self):
        return json.dumps({
            'difficulty': self.difficulty,
            'block_size': self.block_size,
            'blocks': [str(block) for block in self.blocks]
        })

    def save(self, filename: str):
        with open(filename, "w+") as f:
            f.write(str(self))

    @staticmethod
    def from_file(filename: str, entry_type=Entry, validate: bool = True):
        with open(filename, 'r') as f:
            content = f.read()
            data = json.loads(content)
            difficulty = data['difficulty']
            block_size = data['block_size']
            blocks = [Block.from_array(json.loads(block), entry_type) for block in data['blocks']]
            blockchain = Blockchain(difficulty, block_size, blocks)
            if validate and not blockchain.validate():
                raise Exception('Blockchain is not valid')
            return blockchain

    def validate(self):
        for i in range(1, len(self.blocks)):
            if self.blocks[i-1].get_hash() != self.blocks[i].previous_hash:
                return False
        return True

    def get_block_count(self):
        return len(self.blocks)

    def get_entry_count(self):
        return sum([block.get_entry_count() for block in self.blocks])

