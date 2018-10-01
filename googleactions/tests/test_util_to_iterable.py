from googleactions.utils import to_iterable
from unittest.mock import Mock


def test_to_iterable_none():
    assert to_iterable(None) is None


def test_to_iterable_string():
    assert to_iterable('string') == ['string']


def test_to_iterable_object():
    obj = Mock()
    assert to_iterable(obj) == [obj]


def test_to_iterable_strings_list():
    assert to_iterable(['1', '2', '3']) == ['1', '2', '3']


def test_to_iterable_strings_tuple():
    assert to_iterable(('1', '2', '3')) == ('1', '2', '3')