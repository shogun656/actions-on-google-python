from googleactions import Suggestions
from unittest.mock import Mock, MagicMock


def test_init():
    suggestions = Suggestions('a', 'b', 'c')
    sugs = suggestions.suggestions
    assert len(vars(suggestions)) == 1
    assert sugs[0].title == 'a'
    assert sugs[1].title == 'b'
    assert sugs[2].title == 'c'


def test_add_is_added():
    suggestions = Suggestions('a', 'b', 'c')
    response = Mock()
    sugs = []
    response.get_suggestions = MagicMock(return_value=sugs)
    suggestions.add(response)
    assert sugs == [{'title': 'a'}, {'title': 'b'}, {'title': 'c'}]
