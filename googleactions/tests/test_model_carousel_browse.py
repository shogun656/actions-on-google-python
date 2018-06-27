from googleactions import CarouselBrowse, ImageDisplayOptions
from unittest.mock import Mock, MagicMock


def test_init():
    items = [Mock()]
    carousel_browse = CarouselBrowse(items=items, image_display_options='DEFAULT')
    assert len(vars(carousel_browse)) == 2
    assert carousel_browse.items == items
    assert carousel_browse.image_display_options == 'DEFAULT'


def test_dict_is_equal():
    item = Mock()
    item.dict = MagicMock(return_value={'title': 'title'})
    carousel_browse = CarouselBrowse(items=item, image_display_options='DEFAULT')
    assert carousel_browse.dict() == {'items': [{'title': 'title'}], 'imageDisplayOptions': 'DEFAULT'}


def test_add_is_added():
    item = Mock()
    item.dict = MagicMock(return_value={'title': 'title'})
    carousel_browse = CarouselBrowse(items=item, image_display_options='DEFAULT')
    items = []
    response = Mock()
    response.get_items = MagicMock(return_value=items)
    carousel_browse.dict = MagicMock(return_value={'items': [{'title': 'title'}], 'imageDisplayOptions': 'DEFAULT'})
    carousel_browse.add(response)
    assert items == [{'carouselBrowse': {'items': [{'title': 'title'}], 'imageDisplayOptions': 'DEFAULT'}}]
