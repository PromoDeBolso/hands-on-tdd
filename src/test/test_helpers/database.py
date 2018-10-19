import dataset

class DatabaseTestHelper(object):
    @staticmethod
    def clean_table(table_name):
        db = dataset.connect('mysql://mysql:root@db/tdd')
        db[table_name].delete()

    @staticmethod
    def query(statament):
        db = dataset.connect('mysql://mysql:root@db/tdd')
        rows = db.query(statament)

        parsed_rows = []

        for row in rows:
            parsed_rows.append(row)

        return parsed_rows

