from config import *
from exceptions import *
import re
import os
import sqlite3
'''create_table_re = re.findall(r'CREATE TABLE \w+\((\w+ \w+(?:, )?)+\)')''' # for the future


class Database:
    def __init__(self, db_name):
        self.database = db_name
        self.connect = self.create_database()



    def create_database(self, db_name = None): # This function create and open new database
        if db_name == None:
            db_name = self.database
        db_connect = sqlite3.connect(db_name + '.db')

        return db_connect



    def execute_query(self, dbname = None, query = None, save = None): # This function executes the queries that will be entered
        if dbname == None:
            connect = self.create_database(dbname)
        else:
            connect = self.create_database(self.database)
        cur = connect.cursor()

        try:
            first_query_word = str(query).split()[0].upper()
            if first_query_word == 'SELECT': # This "if" returns everything that matches the SELECT-query 
                return cur.execute(query).fetchall()
            
            if save == True: # This "if" needs to save the query
                return query
            
            cur.execute(query)
            connect.commit() # Commit needs to save result of the query    
        
        except sqlite3.OperationalError:
            raise QueryError
    
    def execute_queries(self, dbname, queries, save = None): # This function execute some queries or saves them
        connect = self.create_database(dbname)
        cursor = connect.cursor()

        if bool(save) == True:
            with open('Queries.txt', 'w') as file:
                for query in queries:
                    file.write(query)
                file.close()
        else:
            cursor.executescript(queries)
            connect.commit()
            cursor.close()



    def save_txt_queries(self, query, old_db_name, new_db_name): # This function save queries in text file.
                                                                 #(For migration)
        with open('Queries.txt', 'w') as file:
            file.write(str(self.execute_queries(str(query).replace(old_db_name, new_db_name), True)))
            file.close()
    
    def read_txt_file(self): # This function reads Queries.txt
        with open('Queries.txt', 'r') as file:
            result = file.read()
            file.close()
        return result
    
    def migration_function(self, new_db_name): # This function needs to 'copy' database queries
        queries = self.read_txt_file()
        self.execute_queries(self, new_db_name, queries)



    def select_object(self, table_name, column_list = '*',
                      condition = ''): # This function select objects from table
        try:
            if len(condition) == 0:
                query_result = self.execute_query(f'SELECT {column_list} FROM {table_name}')
            else:
                query_result = self.execute_query(f'SELECT {column_list} FROM {table_name} WHERE {condition}')
            return query_result
        except sqlite3.OperationalError:
            raise TableNotFoundError




    def drop_database(self, database): # This function drop database
        self.execute_query(f"DROP DATABASE {database}")
    
    def drop_object(self, object_type, object_name): # This function drop object in databse
        self.execute_query(f"DROP {object_type.upper()} {object_name}")

db = Database('test')
db.migration_function('test2')
'''
TODO
ДОДЕЛАЙ МИГРАЦИю
РАЗБЕРИСЬ В ИМЕНАХ ПЕРЕМЕННих
'''