from blockchain import Blockchain
from entry import Entry
import random


class TestProductEntry(Entry):

    def __init__(self, serial: str, employee: str, timestamp: int):
        super().__init__()
        self.serial = serial
        self.employee = employee
        self.timestamp = timestamp

    def to_array(self):
        return {
            'serial': self.serial,
            'employee': self.employee,
            'timestamp': self.timestamp
        }

    @staticmethod
    def from_array(data: dict):
        return TestProductEntry(data['serial'], data['employee'], data['timestamp'])


difficulty = 4

block_size = 10


blockchain = Blockchain(difficulty, block_size)

for i in range(123):
    entry = TestProductEntry('60125-0-%s-1' % i, 'SCHNEIDER', random.uniform(0, 100))
    print(' [+] Add entry %s' % entry.get_hash())
    blockchain.add_entry(entry)

blockchain.save('blockchain.db')

blockchain = Blockchain.from_file('blockchain.db', TestProductEntry)

print(' [+] Blockchain contain %s blocks' % blockchain.get_block_count())
print(' [+] Blockchain contain %s entry' % blockchain.get_entry_count())
print(' [+] Blockchain is valid' if blockchain.validate() else print(' [-] Blockchain is not valid'))




