from config import *
from exceptions import *
import re
import os
import sqlite3
'''create_table_re = re.findall(r'CREATE TABLE \w+\((\w+ \w+(?:, )?)+\)')''' # for the future


class Database:
    def __init__(self, db_name):
        self.database = db_name
        self.connect = self.create_database(db_name)

    def create_database(self, db_name): # This function create and open new database
        try:
            dbcon = sqlite3.connect(str(db_name)+'.db') # Database connect
        except: # If name of db doesn't entered, the name of db = self.database
            db_name = str(self.database) + '.db'
            dbcon = sqlite3.connect(db_name)
        return dbcon



    def execute_query(self, dbname = None,
                      query = None, save = None): # This function executes the queries that will be entered
        connect = self.create_database(dbname)
        cur = connect.cursor()

        try:
            cur.execute(query)
            connect.commit() # Commit needs to save result of the query    
        
        except sqlite3.OperationalError:
            raise QueryError
    
    def execute_queries(self, dbname, queries, save = None): # This function execute some queries or saves them
        with self.create_database(dbname) as conn:
            cursor = conn.cursor()

            try:
                cursor.executescript(queries)
                conn.commit()

            except Exception as e:
                conn.rollback()
                raise e

            finally:
                conn.close()



    def save_query(self, query): # This function saves one query
        with open('Saved queries.txt', 'a') as file:
            file.write(f'\nNext query(-ies)\n{query}')
            file.close()
    
    def save_queries(queries): # This function saves some queries
        query_list = queries.split(';')
        query_list = [query.strip() for query in query_list if len(query.strip()) > 0]
        # Create list of not empty queries
        
        queries = '\n'.join(query_list) # Add to every query of the list indent
        
        with open('Saved queries.txt', 'a') as file:
            file.write(f'\nNext query(-ies)\n{queries}')
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

db = Database('test')
db.migration_function('test2')