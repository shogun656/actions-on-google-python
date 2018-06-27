from googleactions import CarouselBrowseItem
from unittest.mock import Mock, MagicMock


def test_init():
    image = Mock()
    carousel_browse_item = CarouselBrowseItem(url='url', title='title',
                                              description='description', image=image, footer='footer')
    assert len(vars(carousel_browse_item)) == 5
    assert carousel_browse_item.open_url_action.url == 'url'
    assert carousel_browse_item.title == 'title'
    assert carousel_browse_item.description == 'description'
    assert carousel_browse_item.image == image
    assert carousel_browse_item.footer == 'footer'


def test_dict_is_equal():
    image = Mock()
    image.dict = MagicMock(return_value={'url': 'url'})
    carousel_browse_item = CarouselBrowseItem(url='url', title='title',
                                              description='description', image=image, footer='footer')
    assert carousel_browse_item.dict() == {'title': 'title',
                                           'description': 'description',
                                           'openUrlAction': {'url': 'url'},
                                           'footer': 'footer',
                                           'image': {'url': 'url'}}
