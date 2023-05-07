from database import Database
from engine import *
from config import *

from tkinter import *

import tkinter.messagebox as mb
import re

window = Tk()

window.geometry(f'{MAIN_WINDOW_WIDTH}x{MAIN_WINDOW_HEIGHT}')
window.resizable(RESIZABLE_WIDTH, RESIZABLE_HEIGHT)
window.title(TITLE)

def open_query_window():
    def send_query(): # This function sends query to the database
        message = mb.askyesno(title='Warning!',
                            message='Are you sure, that you want to send this query?')
        if message:
            database_name = file_name_field.get(0.0, END).strip()
            query = query_field.get(0.0, END).replace('\n', '')
            table_name = re.findall(TABLE_NAME_QUERY, query)
            query = re.findall(REGEX_QUERY, query)
            db = Database(database_name)

            for element in query:
                if 'SELECT' in element:
                    select_status = True
                    break
                else:
                    select_status = False
            if select_status:
                table_name = table_name[0][len('TABLE '):]    
                query_result = db.select_object(table_name, database_name)
                file = open(f'{database_name}_output.txt', 'a+')
                file.write(query_result)
                mb.showinfo(title='Result',
                            message=f'Data was saved as {database_name}_output.txt!')
                file.close()
            else:
                db.execute_queries(query, database_name)
                
            mb.showinfo(title='Result',
                        message='Query was executed!')
    alt_window = Toplevel()
    alt_window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
    alt_window.resizable(RESIZABLE_WIDTH, RESIZABLE_HEIGHT)
    file_name_label = Label(alt_window,
                            text = 'Enter file name below:',
                            width = LABEL_WIDTH,
                            height = LABEL_HEIGHT)

    file_name_field = Text(alt_window,
                           width=ENTRY_WIDTH,
                           height = ENTRY_HEIGHT)

    query_label = Label(alt_window,
                        text = 'Enter query below:',
                        width = LABEL_WIDTH,
                        height = LABEL_HEIGHT)

    query_field = Text(alt_window,
                       width=TEXT_WIDTH,
                       height=TEXT_HEIGHT)

    query_button = Button(alt_window,
                        width=BUTTON_WIDTH,
                        height=BUTTON_HEIGHT,
                        text = 'Send!',
                        command=send_query)

    widgets = [file_name_label,
            file_name_field,
            query_label,
            query_field,
            query_button]

    for widget in widgets:
        widget.pack(anchor='n')

def open_simple_window():
    def send_query(): # This function sends query to the database
        message = mb.askyesno(title='Warning!',
                            message='Are you sure, that you want to send this query?')
        if message:
            database_name = database_field.get(0.0, END).strip()
            table_names_list = tables_field.get(0.0, END).strip().split(',')
            indexes_names_list = indexes_field.get(0.0, END).strip().split(',')
            database = Database(database_name)

            ddl = f'CREATE DATABASE {database_name};\n'

            for table_name in table_names_list:
                ddl += f'CREATE TABLE {table_name};'
            
            for index_name in indexes_names_list:
                ddl += f'CREATE INDEX {index_name};'

            database.execute_queries(ddl, database_name)
                
            mb.showinfo(title='Result',
                        message='Query was executed!')
    simple_window = Toplevel()
    simple_window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
    simple_window.resizable(RESIZABLE_WIDTH, RESIZABLE_HEIGHT)

    database_label = Label(simple_window,
                           text='Enter your database name below:',
                           width=LABEL_WIDTH,
                           height=LABEL_HEIGHT)
    
    database_field = Entry(simple_window, 
                           width=ENTRY_WIDTH)

    tables_label = Label(simple_window, 
                         text='Enter your table names below:')
    tables_field = Text(simple_window, 
                         width=SIMPLE_MODE_TEXT_WIDTH,
                         height=SIMPLE_MODE_TEXT_HEIGHT)

    indexes_label = Label(simple_window,
                          text='Enter your indexes below:')
    indexes_field = Text(simple_window,
                        width=TEXT_WIDTH,
                        height=TEXT_HEIGHT)

    submit_button = Button(simple_window,
                           text='Submit!',
                           width=BUTTON_WIDTH,
                           height=BUTTON_HEIGHT,
                           command=send_query)
    
    widgets = [database_label, database_field,
               tables_label, tables_field,
               indexes_label, indexes_field,
               submit_button]
    
    for widget in widgets:
        widget.pack()

def open_migration_window():
    def migrate():
        ask = mb.askyesno(title='Question',
                          message='Are you sure, that you want to migrate data?')
        if ask:
            new_db_name = target_field.get(0.0, END)
            file_name = file_name_field.get(0.0, END)
            new_db = Database(new_db_name)

    mig_win = Toplevel()
    mig_win.title('Migration')
    mig_win.resizable(RESIZABLE_WIDTH, RESIZABLE_HEIGHT)
    mig_win.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT // 2}')
    target_label = Label(mig_win,
                         width=LABEL_WIDTH,
                         height=LABEL_HEIGHT,
                         text='Enter your new database name below:')
    target_field = Text(mig_win,
                        width=ENTRY_WIDTH,
                        height=ENTRY_HEIGHT)
    file_name_label = Label(mig_win,
                         width=LABEL_WIDTH,
                         height=LABEL_HEIGHT,
                         text='Enter your file name field:')
    file_name_field = Text(mig_win,
                           width=ENTRY_WIDTH,
                           height=ENTRY_HEIGHT)
    start_button = Button(mig_win,
                          width=BUTTON_WIDTH,
                          height=BUTTON_HEIGHT,
                          text='Migrate',
                          command=migrate)
    widgets = [source_label, source_field,
               target_label, target_field,
               file_name_label, file_name_field,
               start_button]
    for widget in widgets:
        widget.pack()

main_label = Label(width=LABEL_WIDTH,
                   height=LABEL_HEIGHT,
                   text='Select your option below.')

empty_label1 = Label(width=LABEL_WIDTH,
                    height = LABEL_HEIGHT)

query_button = Button(width=BUTTON_WIDTH,
                     height=BUTTON_HEIGHT,
                     text='Query Mode',
                     command=open_query_window)

empty_label2 = Label(width=LABEL_WIDTH,
                    height=LABEL_HEIGHT)

simple_button = Button(width=BUTTON_WIDTH,
                       height=BUTTON_HEIGHT,
                       text='Simple Mode',
                       command=open_simple_window)

empty_label3 = Label(width=LABEL_WIDTH,
                     height=LABEL_HEIGHT)

migration_button = Button(width=BUTTON_WIDTH,
                          height=BUTTON_HEIGHT,
                          text = 'Migration',
                          command=open_migration_window)
empty_label4 = Label(width=LABEL_WIDTH,
                     height=LABEL_HEIGHT)

help_button = Button(width=BUTTON_WIDTH,
                     height=BUTTON_HEIGHT,
                     text='Help',
                     command=open_help_link)

widgets = [main_label, empty_label1,
           query_button, empty_label2,
           simple_button, empty_label3,
           migration_button, empty_label4,
           help_button]

for widget in widgets:
    widget.pack()

window.mainloop()