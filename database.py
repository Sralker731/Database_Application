from config import *

import sqlite3

class Database:
    def __init__(self, database_name):
        self.database = database_name

    def create_database(self): # This function create and open new database
        db_connect = sqlite3.connect(self.database + '.db')
        return db_connect
    
    def create_query(self, query = None):
        connect = self.create_database()
        cur = connect.cursor()
        cur.execute(query)

    def select_object(self, object_name, column_list = '*'):
        connect = self.create_database()
        cur = connect.cursor()
        query_result = cur.execute(f'SELECT {column_list} from {object_name}')
        return query_result