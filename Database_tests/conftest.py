import pytest
from Framework.sql_test_functions import *

@pytest.fixture(scope='function')
def func_result():
    db = DatabaseFunctions()
    yield db
    db.drop_object('table', 'table')