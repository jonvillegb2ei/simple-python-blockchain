# simple-python-blockchain

Create a class extending Entry to store your data.

Example:

```python

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

```

Then, create a new blockchain:


```python

difficulty = 4
block_size = 10
blockchain = Blockchain(difficulty, block_size)

```


You can add entry into the blockchain as follow:

```python

entry = TestProductEntry('60125-0-%s-1' % i, 'Employee name', int(time.time() - 1500000 + (3600 * i)))
print(' [+] Add entry %s' % entry.get_hash())
blockchain.add_entry(entry)

```

To save the blockchain:


```python

blockchain.save('/path/to/blockchain.db')

```

To load the blockchain from a file, do:


```python

blockchain = Blockchain.from_file('blockchain.db', TestProductEntry)

```


You can control the blockchain with some methods:

```python

print(' [+] Blockchain contain %s blocks' % blockchain.get_block_count())
print(' [+] Blockchain contain %s entry' % blockchain.get_entry_count())
print(' [+] Blockchain is valid' if blockchain.validate() else print(' [-] Blockchain is not valid'))

```