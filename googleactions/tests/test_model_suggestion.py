from googleactions import Suggestion
from unittest.mock import Mock, MagicMock


def test_init():
    suggestion = Suggestion(title='title')
    assert len(vars(suggestion)) == 1
    assert suggestion.title == 'title'


def test_dict_is_equal():
    suggestion = Suggestion(title='title')
    assert suggestion.dict() == {'title': 'title'}


def test_add_is_added():
    suggestion = Suggestion(title='title')
    response = Mock()
    suggestions = []
    response.get_suggestions = MagicMock(return_value=suggestions)
    suggestion.dict = MagicMock(return_value={'title': 'title'})
    suggestion.add(response)
    assert suggestions == [{'title': 'title'}]
