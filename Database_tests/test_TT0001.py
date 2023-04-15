'''
Test Case #1 
Description: Check, that if you insert into table something, it can be found by Id
Resources: Database

Automated by                Date                        Description
-----------------------------------------------------------------------
Kostantin Rudenko           ...                         Initial version
'''

import pytest
from Framework.config import NAMES

@pytest.mark.TT0001
@pytest.mark.parametrize(['id', 'expected_result'], NAMES)

def test_TT0001(func_result, id, expected_result):
    db = func_result
    result = db.select_object(id)
    assert expected_result in result