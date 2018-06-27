from googleactions import Image


def test_init():
    image = Image(url='url', alt='alt')
    assert len(vars(image)) == 2
    assert image.url == 'url'
    assert image.accessibility_text == 'alt'


def test_dict_is_equal():
    image = Image(url='url', alt='alt')
    assert image.dict() == {'url': 'url', 'accessibilityText': 'alt'}
