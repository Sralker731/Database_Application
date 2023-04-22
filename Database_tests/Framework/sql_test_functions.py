import sqlite3

from Framework.config import *

class DatabaseFunctions:
    def __init__(self, db_name = 'test', table_name = 'table') -> None:
        self.db = db_name
        self.table = table_name
        self.con = sqlite3.connect(self.db + '.db')
        self.cur = self.con.cursor()
    
    def exec(self, query) -> None: # Execute query
        self.cur.execute(query)

        self.con.commit()

    def create_table(self, columns) -> None:
        self.exec(f"CREATE TABLE {self.table}({columns})")

    def insert(self, values):
        self.exec(f"INSERT INTO {self.table}({SELECT_COLUMNS[0]}) VALUES (?, ?)", (values))

    def genarate_index(self, num) -> list[int]:
        result = [x for x in range(num)]
        return result

    def drop_object(self, type, name):
        self.exec(f'DROP {type.upper()} {name}')
        
# Functions for tests

    def select_object(self, id_num):
        self.create_table('id int, name varchar(20)')
        self.insert(NAMES)
        self.exec(f"SELECT * FROM table WHERE id == {str(id_num)}")
        return self.cur.fetchall()[0]