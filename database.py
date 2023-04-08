from config import *
from exceptions import *
import re
'''create_table_re = re.findall(r'CREATE TABLE \w+\((\w+ \w+(?:, )?)+\)')''' # for the future
import sqlite3

class Database:
    def __init__(self, database_name):
        self.database = database_name

    def create_database(self): # This function create and open new database
        db_connect = sqlite3.connect(self.database + '.db')
        return db_connect
    
    def execute_query(self, query = None): # This function executes the queries that will be entered
        connect = self.create_database()
        cur = connect.cursor()
        cur.execute(query)
        connect.commit() # Commit needs to save result of the query
        connect.close()

    def select_object(self, table_name, column_list = '*'): # This function select objects from table
        connect = self.create_database()
        cur = connect.cursor()
        query_result = cur.execute(f'SELECT {column_list} FROM {table_name}')
        return query_result

# below experiments
db = Database('random_shit')
'''
db.create_database()
db.execute_query("CREATE TABLE test(i integer, age int)")
db.execute_query("INSERT INTO test(i, age) VALUES (1, 25), (2, 298), (3, 90243), (4, 112), (5, 895)")'''
for elem in db.select_object('test', '*').fetchone():
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
