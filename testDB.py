'''
This is a file with several tests using the pytest and sqlite3 libraries.

If you don't know how run this file, so I can tell how:
1. Open terminal.
2. Enter `cd Database_Application`
3. Enter `pytest testDB.py -m [mark_name]`.
'''
import pytest
import sqlite3
class DBTests:
    def __init__(self, db_name = 'test_db') -> None:
        self.db = db_name
        self.con = sqlite3.connect(self.db + '.db')
        self.cur = self.con.cursor()
    
    def exec(self, query): # Execute query
        self.cur.execute(query)
        self.con.commit()

    def test_select(self):
        self.cur.exec("CREATE TABLE test(id int, name varchar(20))")
        self.cur.exec(
        "INSERT INTO test(id, name) VALUES (1, 'Dmitriy'), (2, 'Andrew'), (3, 'John'), (4, 'George')")

        self.cur.exec("SELECT * FROM test WHERE id == 1")
        return self.cur.fetchone()