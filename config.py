# Database parameters

DATATYPES = {'integer' : 'INT',
             'boolean' : 'BOOL',
             'varchar' : 'VARCHAR',
             'char'    : 'CHAR'}

KEYS = {'primary_key'  : 'PRIMARY KEY',
        'foreign_key'  : 'FOREIGN KEY'}

OBJECTS = {'database' : 'DATABASE',
           'table' : 'TABLE',
           'index' : 'INDEX'}

# UI Parameters
MAIN_WINDOW_WIDTH = 200
MAIN_WINDOW_HEIGHT = 300

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

BUTTON_WIDTH = 10
BUTTON_HEIGHT = 2

LABEL_WIDTH = 30
LABEL_HEIGHT = 1

ENTRY_WIDTH = 30
ENTRY_HEIGHT = 1

TEXT_WIDTH = 40
TEXT_HEIGHT = 20

SIMPLE_MODE_TEXT_WIDTH = 20
SIMPLE_MODE_TEXT_HEIGHT = 10

RESIZABLE_WIDTH = False
RESIZABLE_HEIGHT = False

TITLE = 'Database Application V.1.0.0'

# Regular expression values
REGEX_QUERY = r'[A-Za-z0-9\w\s|*]+;'
TABLE_NAME_QUERY=r'Table|table|TABLE\s[a-zA-Z0-9]+'
SELECT_QUERY = r"[SELECTselectSelect]+\w|\W+ [fromFromFROM]+ +[A-Za-z0-9]+;|[SELECTselectSelect]+\w|\W+ [fromFromFROM]+ +[A-Za-z0-9]+ +[whereWhereWHERE]+[\w\W]+;"

# Browser values
BROWSERS = ['chrome', 'firefox', 'opera', 'safari']
HELP_LINK = 'https://github.com/Sralker731/Database_Application/wiki' 

# File path & file names
PATH = 'Database_Application\\'
SELECT_FILENAME = 'save'

# Error values
ERROR_VALUES = '!@#$%^&*()/-+*:;~'

# CMD values
EDGE_PROMPT = f'cmd /c python "start msedge {HELP_LINK}"'
WEBBROWSER_PROMPT = f'cmd /c "python -m webbrowser -t "{HELP_LINK}""'

# Query command words
SELECT_WORDS = ['SELECT', 'Select', 'select']