import webbrowser
import os
import re

from config import *

def open_help_link():
    try:
        os.system(WEBBROWSER_PROMPT)
    except:
        os.system(EDGE_PROMPT)
    
def save_query(text_query):
    file_name = 'QUERIES_0.txt'
    while os.path.exists(PATH + f'\\{file_name}'):
        start_border = file_name.find('_') 
        end_border = file_name.find('.')
        number = int(file_name[start_border + 1:end_border]) 
        file_name = file_name.replace(str(number), str(number + 1))
    file = open(file_name, 'w')
    file.write(text_query)
    file.close()
    return file_name

def read_txt_file(file_name): # This function reads file
    with open(file_name +'.txt', 'r') as file:
        result = file.read()
        file.close()
    return result

def save_txt_file(data, file_name):
    with open(file_name + '.txt', 'w') as file:
        file.write(file_name)
        file.close()

def find_select_stmt(query):
    select_values = re.match(SELECT_QUERY, query).group()
    select_query = ''
    #for value in select_values:
    #    select_query += value + '\n'
    return select_values