from googleactions.models import MediaObject
from unittest.mock import Mock, MagicMock


def test_init():
    icon = Mock()
    large_image = Mock()
    media_object = MediaObject(name='name', description='description', url='www.google.com',
                               icon=icon, large_image=large_image)
    assert len(vars(media_object)) == 5
    assert media_object.name == 'name'
    assert media_object.description == 'description'
    assert media_object.content_url == 'www.google.com'
    assert media_object.icon == icon
    assert media_object.large_image == large_image


def test_dict_is_equal():
    icon = Mock()
    icon.dict = MagicMock(return_value={'url': 'url', 'accessibilityText': 'alt'})
    large_image = Mock()
    large_image.dict = MagicMock(return_value={'url': 'url', 'accessibilityText': 'alt'})
    media_object = MediaObject(name='name', description='description', url='www.google.com',
                               icon=icon, large_image=large_image)
    assert media_object.dict() == {'name': 'name',
                                   'description': 'description',
                                   'contentUrl': 'www.google.com',
                                   'icon': {'url': 'url', 'accessibilityText': 'alt'},
                                   'largeImage': {'url': 'url', 'accessibilityText': 'alt'}}
