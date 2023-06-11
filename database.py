from config import *
from exceptions import *

import re
import os
import sqlite3
'''create_table_re = re.findall(r'CREATE TABLE \w+\((\w+ \w+(?:, )?)+\)')''' # for the future


class Database:
    def __init__(self, db_name):
        self.database = db_name
        self.connect = sqlite3.connect(self.database+'.db')

    def create_database(self, db_name, conn_return = False):
        # This function create new database and return connection to it
        try:
            dbcon = sqlite3.connect(str(db_name)+'.db') # Database connect
            return dbcon
        except: # If name of db doesn't entered, the name of db = self.database
            db_name = str(self.database) + '.db'
            dbcon = sqlite3.connect(db_name)
            #if conn_return == True: # FixMe
            return dbcon

    def execute_query(self, dbname = None,
                      query = None, connection_status = False): 
        # This function executes the queries that will be entered
        #connect = self.create_database(dbname, connection_status)
        cur = self.connect.cursor()

        try:
            cur.execute(query)
            self.connect.commit() # Commit needs to save result of the query    
        
        except sqlite3.OperationalError:
            raise QueryError
    
    def execute_queries(self, dbname, queries): # This function execute some queries or saves them
        #conn = self.create_database(dbname)
        cursor = self.connect.cursor()

        #try:
        cursor.executescript(queries)
        self.connect.commit()
        '''
        except Exception as e:
            conn.rollback()
            raise e
        '''
        self.connect.close()


    def migration_function(self, dbname, queries): # This function needs to 'copy' database queries
        self.create_database(dbname)
        self.execute_queries(dbname, queries)


    def select_object(self, table_name, column_list = '*',
                      condition = '', connect_status = False): # This function select objects from table
        try:
            if len(condition) == 0:
                query_result = self.execute_query(f'SELECT {column_list} FROM {table_name}', connect_status)
            else:
                query_result = self.execute_query(f'SELECT {column_list} FROM {table_name} WHERE {condition}',
                                                  connect_status)
            return query_result
        except sqlite3.OperationalError:
            raise TableNotFoundError