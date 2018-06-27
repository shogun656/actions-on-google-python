from googleactions import SimpleResponse
from unittest.mock import MagicMock, Mock


def test_init():
    simple_response = SimpleResponse(speech='speech', ssml='<speak>ssml</speak>', text='text')
    assert len(vars(simple_response)) == 3
    assert simple_response.speech == 'speech'
    assert simple_response.ssml == '<speak>ssml</speak>'
    assert simple_response.text == 'text'


def test_dict_is_equal():
    simple_response_dict = SimpleResponse(speech='speech', ssml='<speak>ssml</speak>', text='text').dict()
    assert simple_response_dict == {'textToSpeech': 'speech', 'ssml': '<speak>ssml</speak>', 'displayText': 'text'}


def test_get_index_is_0():
    items = [{'simpleResponse': {}}]
    assert SimpleResponse.get_index(items) == 0


def test_get_index_is_1():
    items = [{'item': {}}, {'simpleResponse': {}}]
    assert SimpleResponse.get_index(items) == 1


def test_get_simple_index_is_none():
    assert SimpleResponse.get_index([]) is None


def test_add_is_added():
    simple_response = SimpleResponse(speech='speech', ssml='<speak>ssml</speak>', text='text')
    simple_response.dict = \
        MagicMock(return_value={'textToSpeech': 'speech', 'ssml': '<speak>ssml</speak>', 'displayText': 'text'})
    items = [{'simpleResponse': {'textToSpeech': '1', 'ssml': '2', 'displayText': '3'}}]
    response = Mock()
    response.get_items = MagicMock(return_value=items)
    simple_response.add(response)
    assert items == [{'simpleResponse':
                     {'textToSpeech': '1', 'ssml': '2', 'displayText': '3'}},
                     {'simpleResponse':
                     {'textToSpeech': 'speech', 'ssml': '<speak>ssml</speak>', 'displayText': 'text'}}]
