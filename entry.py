import hashlib
import json


class Entry:

    def __init__(self):
        pass

    def to_array(self):
        return { }

    @staticmethod
    def from_array(data: dict):
        return Entry()

    def get_hash(self):
        data = json.dumps(self.to_array())
        m = hashlib.sha256()
        m.update(data.encode())
        return m.hexdigest()

    def __str__(self):
        data = self.to_array()
        data['hash'] = self.get_hash()
        return json.dumps(data)



