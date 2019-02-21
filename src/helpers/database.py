import dataset

class DatabaseHelper(object):
    def __init__(self, table):
        self.db = dataset.connect('mysql://mysql:root@db/tdd')
        self.table = self.db[table]

    def insert(self, data):
        self.table.insert(data)

    def find_one(self, query):
        return self.table.find_one(query)



