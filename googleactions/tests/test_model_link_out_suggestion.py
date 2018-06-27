from googleactions import LinkOutSuggestion
from unittest.mock import Mock, MagicMock


def test_init():
    link_out_suggestion = LinkOutSuggestion(name='name', url='url')
    assert len(vars(link_out_suggestion)) == 2
    assert link_out_suggestion.destination_name == 'name'
    assert link_out_suggestion.open_url_action.url == 'url'


def test_dict_is_equal():
    link_out_suggestion = LinkOutSuggestion(name='name', url='url')
    assert link_out_suggestion.dict() == {'destinationName': 'name',
                                          'url': 'url',
                                          'openUrlAction': {'url': 'url'}}


def test_add_is_added():
    link_out_suggestion = LinkOutSuggestion(name='name', url='url')
    response = Mock()
    rich = {}
    response.get_rich_response = MagicMock(return_value=rich)
    link_out_suggestion.dict = MagicMock(return_value={'destinationName': 'name',
                                                       'url': 'url',
                                                       'openUrlAction': {'url': 'url'}})
    link_out_suggestion.add(response)
    assert rich == {'linkOutSuggestion': {'destinationName': 'name',
                                          'url': 'url',
                                          'openUrlAction': {'url': 'url'}}}
