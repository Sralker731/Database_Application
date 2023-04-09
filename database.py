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
    
    def execute_query(self, query = None): # This function executes the queries that will be entered
        connect = self.create_database()
        cur = connect.cursor()
        try:
            cur.execute(query)
            if 'SELECT' in query:
                return cur.fetchall()
            connect.commit() # Commit needs to save result of the query
            connect.close()            
        except sqlite3.OperationalError:
            raise QueryError

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
    def drop_database(self):
        self.execute_query(f"DROP DATABASE {self.database}")
    
    def drop_object(self, object_type, object_name):
        self.execute_query(f"DROP {object_type.upper()} {object_name}")

# below experiments
db = Database('random_shit')

db.create_database()
db.execute_query("CREATE TABLE test(i integer, name varchar(20))")
#db.drop_object('table', 'test')
db.execute_query("INSERT INTO test(i, name) VALUES (1, 'dima'), (2, 'jawdji'), (3, 'hoe'), (4, 'oihfaew'), (5, 'you')")
for elem in db.select_object('test', 'i = 3'):
    print(elem)
# TODO
"""
1. Залить первую НЕДОверсию в гитхаб +
2. Поэкспериментировать с запросами в базу данных +
3. Решить баг, который создает базу вне рамок репозитория ---
4. Создать функции (выбрать 1 объект, много и все) = fetchmany([count])
5. Создать файл exceptions.py и прописать ошибки: +
    Query Error
    Database\Table\Index not found error 
6. Составить документацию по продукту +
7. Залить отдельной веткой (db)
"""
