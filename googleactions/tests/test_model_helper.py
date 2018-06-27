from googleactions import Helper, SimpleResponse
from unittest.mock import MagicMock, Mock


def setup_module(module):
    module.get_index = SimpleResponse.get_index


def teardown_module(module):
    SimpleResponse.get_index = module.get_index


def test_add_simple_does_add():
    items = []
    response = Mock()
    response.get_items = MagicMock(return_value=items)
    SimpleResponse.get_index = MagicMock(return_value=None)
    Helper.add_simple(response)
    assert items == [{'simpleResponse': {'textToSpeech': '~'}}]


def test_add_simple_does_not_add():
    items = [{'simpleResponse': {'textToSpeech': 'speech'}}]
    response = Mock()
    response.get_items = MagicMock(return_value=items)
    SimpleResponse.get_index = MagicMock(return_value=0)
    Helper.add_simple(response)
    assert items == [{'simpleResponse': {'textToSpeech': 'speech'}}]
