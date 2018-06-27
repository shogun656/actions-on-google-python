from googleactions import List
from unittest.mock import Mock, MagicMock


def test_init():
    items = [Mock(), Mock(), Mock()]
    list = List(title='title', items=items)
    assert len(vars(list)) == 2
    assert list.title == 'title'
    assert list.items == items


def test_dict_is_equal():
    item = Mock()
    item.dict = MagicMock(return_value={'title': 'title'})
    items = [item, item, item]
    list = List(title='title', items=items)
    assert list.dict() == {'intent': 'actions.intent.OPTION',
                           'data': {'@type': 'type.googleapis.com/google.actions.v2.OptionValueSpec',
                                    'listSelect': {'items':
                                                   [{'title': 'title'},
                                                    {'title': 'title'},
                                                    {'title': 'title'}],
                                                   'title': 'title'}}}


def test_add_is_added():
    response = Mock()
    payload = {}
    response.get_google_payload = MagicMock(return_value=payload)
    item = Mock()
    item.dict = MagicMock(return_value={'title': 'title'})
    list = List(title='title', items=item)
    list.dict = MagicMock(return_value={'intent': 'actions.intent.OPTION',
                                        'data': {'@type': 'type.googleapis.com/google.actions.v2.OptionValueSpec',
                                                 'listSelect': {'items':
                                                                [{'title': 'title'}],
                                                                'title': 'title'}}})
    list.add(response)
    assert payload == {'systemIntent': {'intent': 'actions.intent.OPTION',
                                        'data': {'@type': 'type.googleapis.com/google.actions.v2.OptionValueSpec',
                                                 'listSelect': {'items': [{'title': 'title'}],
                                                                'title': 'title'}}}}
