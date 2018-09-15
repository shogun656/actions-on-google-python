from googleactions import AppResponse, utils, Storage, End
from unittest.mock import Mock, MagicMock


def setup_module(module):
    module.add_items = AppResponse.add_items
    module.flatten = utils.flatten
    module.add_end_item = AppResponse.add_end_item
    global MODULE
    MODULE = module


def teardown_module(module):
    AppResponse.add_items = module.add_items
    utils.flatten = module.flatten
    AppResponse.add_end_item = module.add_end_item


def test_init():
    AppResponse.add_items = MagicMock()
    items = Mock()
    app_request = Mock()
    app_response = AppResponse(items=items, app_request=app_request)
    assert app_response.response == {
        'payload':
            {
                'google': {
                    'expectUserResponse': True,
                    'richResponse': {
                        'items': []
                    }
                }
            }
    }
    assert app_response.app_request == app_request
    assert AppResponse.add_items.call_count == 1


def test_add_items_add_string():
    utils.flatten = MagicMock(return_value=['str'])
    AppResponse.add_items = MODULE.add_items
    app_response = AppResponse(items='str')
    assert app_response.response == {
        'payload':
            {
                'google': {
                    'expectUserResponse': True,
                    'richResponse': {
                        'items': [{'simpleResponse': {'textToSpeech': 'str'}}]
                    }
                }
            }
    }


def test_add_items_add_storage():
    storage = Storage()
    storage.add = MagicMock()
    app_request = Mock()
    utils.flatten = MagicMock(return_value=[storage])
    app_response = AppResponse(items=storage, app_request=app_request)
    assert storage.add.call_count == 1


def test_add_items_add_end():
    end = End()
    end.add = MagicMock()
    utils.flatten = MagicMock(return_value=[end])
    app_response = AppResponse(items=end)
    assert end.add.call_count == 1


def test_add_items_add_item():
    item = Mock()
    item.add = MagicMock()
    utils.flatten = MagicMock(return_value=[item])
    app_response = AppResponse(items=item)
    assert item.add.call_count == 1


def test_add_end_item():
    AppResponse.needs_end = MagicMock(return_value=True)
    AppResponse.add_items = MagicMock()
    app_response = AppResponse(items=None)
    AppResponse.add_end_item(app_response, has_end=False, app_request=None)
    assert app_response.response == {
        'payload':
            {
                'google': {
                    'expectUserResponse': False,
                    'richResponse': {
                        'items': []
                    }
                }
            }
    }


def test_needs_end():
    app_request = Mock()
    app_request.is_intent = MagicMock(return_value=True)
    assert AppResponse.needs_end(app_request) is True


def test_get_google_payload():
    AppResponse.add_items = MagicMock()
    app_response = AppResponse(items=None)
    google = app_response.get_google_payload()
    assert google == {
        'expectUserResponse': True,
        'richResponse': {
            'items': []
        }
    }


def test_get_rich_response():
    AppResponse.add_items = MagicMock()
    app_response = AppResponse(items=None)
    rich = app_response.get_rich_response()
    assert rich == {
        'items': []
    }


def test_get_suggestions():
    AppResponse.add_items = MagicMock()
    app_response = AppResponse(items=None)
    rich = {'items': []}
    app_response.get_rich_response = MagicMock(return_value=rich)
    assert app_response.get_suggestions() == []
    assert rich == {'items': [], 'suggestions': []}


def test_get_items():
    AppResponse.add_items = MagicMock()
    app_response = AppResponse(items=None)
    arr = []
    rich = {'items': arr}
    app_response.get_rich_response = MagicMock(return_value=rich)
    assert app_response.get_items() == arr


def test_json():
    AppResponse.add_items = MagicMock()
    app_response = AppResponse(items=None)
    assert app_response.json() == '{"payload": {"google": {"expectUserResponse": true, "richResponse": {"items": []}}}}'
