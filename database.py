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

db = Database('random_shit')
db.create_database()
#db.create_query("""CREATE TABLE test(i integer)""")
#db.create_query("""INSERT INTO test(i) VAlUES (1)""")

print(db.select_object('test', '*'))

# TODO
1. Залить первую НЕДОверсию в гитхаб
2. Поэкспериментировать с запросами в базу данных
3. Решить баг, который создает базу вне рамок репозитория
4. Создать функции (выбрать 1 объект, много и все)
5. Создать файл exceptions.py и прописать ошибки:
    Query Error 
    Database\Table\Index not found error 
6. Составить документацию по продукту
7. Залить отдельной веткой (db)

