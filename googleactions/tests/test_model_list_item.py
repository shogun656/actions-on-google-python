from googleactions import ListItem
from unittest.mock import Mock, MagicMock


def test_init():
    image = Mock()
    synonyms = ['a', 'b', 'c']
    list_item = ListItem(key='key', title='title', description='description', image=image, synonyms=synonyms)
    assert len(vars(list_item)) == 5
    assert list_item.key == 'key'
    assert list_item.title == 'title'
    assert list_item.description == 'description'
    assert list_item.image == image
    assert list_item.synonyms == synonyms


def test_dict_is_equal():
    image = Mock()
    image.dict = MagicMock(return_value={'url': 'url'})
    synonyms = ['a', 'b', 'c']
    list_item = ListItem(key='key', title='title', description='description', image=image, synonyms=synonyms)
    assert list_item.dict() == {'title': 'title', 'description': 'description',
                                'image': {'url': 'url'}, 'optionInfo': {'key': 'key', 'synonyms': ['a', 'b', 'c']}}
