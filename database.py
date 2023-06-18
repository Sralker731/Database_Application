from config import *
from exceptions import *
from engine import *

import re
import os
import sqlite3


class Database:
    def __init__(self, db_name):
        self.database = db_name
        self.connect = sqlite3.connect(self.database+'.db')

    def create_database(self, db_name):
        # This function create new database and return connection to it
        try:
            dbcon = sqlite3.connect(str(db_name)+'.db') # Database connect
            return dbcon
        except: # If name of db doesn't entered, the name of db = self.database
            db_name = str(self.database) + '.db'
            dbcon = sqlite3.connect(db_name)
            return dbcon

    def execute_query(self, query = None): 
        cur = self.connect.cursor()

        try:
            cur.execute(query)
            self.connect.commit() # Commit needs to save result of the query    
        
        except sqlite3.OperationalError:
            raise QueryError
    
    def execute_queries(self, queries): # This function execute some queries or saves them
        cursor = self.connect.cursor()
        cursor.executescript(queries)
        self.connect.commit()
        #self.connect.close()


    def migration_function(self, dbname, queries): # This function needs to 'copy' database queries
        self.create_database(dbname)
        self.execute_queries(dbname, queries)


    def select_object(self, query): # This function select objects from table
        try:
            queries = find_select_stmt(query)
            result = self.execute_queries(queries)
            return result
        except sqlite3.OperationalError:
            raise TableNotFoundError