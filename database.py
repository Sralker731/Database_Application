from config import *
from exceptions import *
import re
import os
import sqlite3
'''create_table_re = re.findall(r'CREATE TABLE \w+\((\w+ \w+(?:, )?)+\)')''' # for the future


class Database:
    def __init__(self, database_name):
        self.database = database_name

    def create_database(self): # This function create and open new database
        db_connect = sqlite3.connect(self.database + '.db')

        return db_connect
    
    def connect_database(self, database):
        db_con = sqlite3.connect(database + '.db')
        return db_con
    
    def execute_query(self, query = None, save = None): # This function executes the queries that will be entered
        connect = self.create_database()
        cur = connect.cursor()

        try:
            cur.execute(f'''{query}''')
            if 'SELECT' in query:
                return cur.fetchall()
            
            if save == True:
                return query
            
            connect.commit() # Commit needs to save result of the query    
        
        except sqlite3.OperationalError:
            raise QueryError
    
    def execute_queries(self, query): # This function execute some queries
        for queries in query:
            self.execute_query(queries, True)

    def save_txt_queries(self, query): # This function save queries in text file
        result = self.execute_queries(query)
        with open('Queries.txt', 'w') as file:
            file.write(str(result))
            file.close()
    
    def migration_function(self, migrationDB): # This function needs to 'copy' database queries
        self.connect_database(migrationDB)
        with open('Queries.txt', 'r') as file:
            result = file.read()
            self.execute_queries(result)
            file.close()

    def select_object(self, table_name, 
                      condition = '', column_list = '*'): # This function select objects from table
        connect = self.create_database()
        cur = connect.cursor()
        try:
            if len(condition) == 0:
                query_result = self.execute_query(f'SELECT {column_list} FROM {table_name}')
            else:
                query_result = self.execute_query(f'SELECT {column_list} FROM {table_name} WHERE {condition}')
            return query_result
        except sqlite3.OperationalError:
            raise TableNotFoundError

    def drop_database(self): # This function drop database
        self.execute_query(f"DROP DATABASE {self.database}")
    
    def drop_object(self, object_type, object_name): # This function drop object in databse
        self.execute_query(f"DROP {object_type.upper()} {object_name}")