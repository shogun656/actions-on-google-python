from googleactions.utils import get_or_create_array
from unittest.mock import Mock


def test_get_or_create_array_no_key():
    dict = {'key1': 'value1'}
    assert get_or_create_array(dict, 'key2') == []
    assert dict == {'key1': 'value1', 'key2': []}


def test_get_or_create_array_has_key():
    dict = {'key1': 'value1', 'key2': 'value2'}
    assert get_or_create_array(dict, 'key2') == ['value2']
    assert dict == {'key1': 'value1', 'key2': ['value2']}


def test_get_or_create_array_no_key_objects():
    obj1 = Mock()
    dict = {'key1': obj1}
    assert get_or_create_array(dict, 'key2') == []
    assert dict == {'key1': obj1, 'key2': []}


def test_get_or_create_array_has_key_objects():
    obj1 = Mock()
    obj2 = Mock()
    dict = {'key1': obj1, 'key2': obj2}
    assert get_or_create_array(dict, 'key2') == [obj2]
    assert dict == {'key1': obj1, 'key2': [obj2]}
