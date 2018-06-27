from googleactions import MediaResponse
from unittest.mock import Mock, MagicMock


def test_init():
    media_objects = [Mock()]
    media_type = 'AUDIO'
    media_response = MediaResponse(media_objects=media_objects, media_type=media_type)
    assert len(vars(media_response)) == 2
    assert media_objects == media_response.media_objects
    assert media_type == media_response.media_type


def test_dict_is_equal():
    media_object = Mock()
    media_object.dict = MagicMock(return_value={'name': 'name'})
    media_objects = [media_object]
    media_type = 'AUDIO'
    media_response = MediaResponse(media_objects=media_objects, media_type=media_type)
    assert media_response.dict() == {'mediaType': 'AUDIO', 'mediaObjects': [{'name': 'name'}]}


def test_add_is_added():
    media_response = MediaResponse(media_objects=Mock(), media_type=Mock())
    media_response.dict = MagicMock(return_value={'mediaType': 'AUDIO', 'mediaObjects': [{'name': 'name'}]})
    items = []
    response = Mock()
    response.get_items = MagicMock(return_value=items)
    media_response.add(response)
    assert items == [{'mediaResponse': {'mediaType': 'AUDIO', 'mediaObjects': [{'name': 'name'}]}}]
