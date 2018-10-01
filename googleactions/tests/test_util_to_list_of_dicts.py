from googleactions.utils import to_list_of_dicts
from unittest.mock import Mock, MagicMock


def test_to_list_of_dicts():
    obj1 = Mock()
    dict1 = {'key1': 'value1'}
    obj2 = Mock()
    dict2 = {'key2': 'value2'}
    obj1.dict = MagicMock(return_value=dict1)
    obj2.dict = MagicMock(return_value=dict2)
    assert to_list_of_dicts([obj1, obj2]) == [{'key1': 'value1'}, {'key2': 'value2'}]
