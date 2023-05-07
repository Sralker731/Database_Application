import webbrowser
import os

from config import *

def open_help_link():
    browser_pos = 0
    def open_browser(pos = browser_pos):
        try:
            webbrowser.get(BROWSERS[pos]).open(HELP_LINK)
        except IndexError:
            if pos <= len(BROWSERS) - 1:
                pos += 1
                open_browser(pos)
            else:
                return None
    
def save_query(text_query):
    file_name = 'QUERIES_0.txt'
    while os.path.exists(PATH + f'/{file_name}'):
        start_border = file_name.find('_') 
        end_border = file_name.find('.')
        number = int(file_name[start_border + 1:end_border]) 
        file_name = file_name.replace(str(number), str(number + 1))
    file = open(file_name, 'w')
    file.write(text_query)
    file.close()
    return file_name
    