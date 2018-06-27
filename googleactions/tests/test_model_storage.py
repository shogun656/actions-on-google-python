from googleactions import Storage
from unittest.mock import Mock, MagicMock


def test_init_from_kwargs():
    storage = Storage(key_a='a', key_b='b', key_c='c')
    assert storage.dictionary == {'key_a': 'a', 'key_b': 'b', 'key_c': 'c'}
    assert storage.overwrite is False


def test_init_from_dict_kwargs():
    storage = Storage(**{'key_a': 'a', 'key_b': 'b', 'key_c': 'c'})
    assert storage.dictionary == {'key_a': 'a', 'key_b': 'b', 'key_c': 'c'}
    assert storage.overwrite is False


def test_init_from_dict():
    storage = Storage({'key_a': 'a', 'key_b': 'b', 'key_c': 'c'})
    assert storage.dictionary == {'key_a': 'a', 'key_b': 'b', 'key_c': 'c'}
    assert storage.overwrite is False


def test_init_from_dict_with_overwrite():
    storage = Storage(dictionary={'key_a': 'a', 'key_b': 'b', 'key_c': 'c'}, overwrite=True)
    assert storage.dictionary == {'key_a': 'a', 'key_b': 'b', 'key_c': 'c'}
    assert storage.overwrite is True


def test_init_from_none():
    storage = Storage(None)
    assert len(storage.dictionary) == 0
    assert storage.overwrite is False


def test_add_has_added():
    storage = Storage(key_a='a', key_b='b', key_c='c')
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    storage.add(response)
    assert payload == {'userStorage': '{"key_a": "a", "key_b": "b", "key_c": "c"}'}


def test_add_has_added_none_with_empty_dict():
    storage = Storage({})
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    storage.add(response)
    assert payload == {'userStorage': '{}', 'resetUserStorage': True}


def test_add_has_added_none_with_none():
    storage = Storage(None)
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    storage.add(response)
    assert payload == {'userStorage': '{}', 'resetUserStorage': True}


def test_add_has_added_none_with_none():
    storage = Storage(None)
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    storage.add(response)
    assert payload == {'userStorage': '{}', 'resetUserStorage': True}


def test_add_has_added_none_with_no_args():
    storage = Storage()
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    storage.add(response)
    assert payload == {'userStorage': '{}', 'resetUserStorage': True}


def test_add_with_overwrite_false_no_equest():
    storage = Storage(key_a='a')
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    storage.add(response)
    assert payload == {'userStorage': '{"key_a": "a"}'}


def test_add_with_overwrite_false():
    storage = Storage(key_a='a')
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    request = Mock()
    request.get_storage = MagicMock(return_value={'key_b': 'b', 'key_c': 'c'})
    storage.add(response, request)
    assert payload == {'userStorage': '{"key_a": "a", "key_b": "b", "key_c": "c"}'}


def test_add_with_overwrite_true():
    storage = Storage(key_a='a', overwrite=True)
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    request = Mock()
    request.get_storage = MagicMock(return_value={'key_b': 'b', 'key_c': 'c'})
    storage.add(response, request)
    assert payload == {'userStorage': '{"key_a": "a"}'}
