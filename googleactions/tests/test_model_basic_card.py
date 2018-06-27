from googleactions import BasicCard
from unittest.mock import MagicMock, Mock


def test_init():
    button = Mock()
    buttons = [button, button]
    image = Mock()
    image_display_options = Mock()
    basic_card = BasicCard(title='title',
                           subtitle='subtitle',
                           text='text',
                           image=image,
                           buttons=buttons,
                           image_display_options=image_display_options)
    assert len(vars(basic_card)) == 6
    assert basic_card.title == 'title'
    assert basic_card.subtitle == 'subtitle'
    assert basic_card.formatted_text == 'text'
    assert basic_card.image == image
    assert basic_card.buttons == buttons
    assert basic_card.image_display_options == image_display_options


def test_dict_is_equal():
    button = Mock()
    button.dict = MagicMock(return_value={'title': 'title', 'openUrlAction': 'url'})
    buttons = [button, button]
    image = Mock()
    image.dict = MagicMock(return_value={'url': 'url', 'accessibilityText': 'alt'})
    basic_card = BasicCard(title='title',
                           subtitle='subtitle',
                           text='text',
                           image=image,
                           buttons=buttons,
                           image_display_options='DEFAULT')
    assert basic_card.dict() == {'title': 'title',
                                 'subtitle': 'subtitle',
                                 'formattedText': 'text',
                                 'image': {'url': 'url', 'accessibilityText': 'alt'},
                                 'buttons': [{'title': 'title', 'openUrlAction': 'url'},
                                             {'title': 'title', 'openUrlAction': 'url'}],
                                 'imageDisplayOptions': 'DEFAULT'}


def test_add_is_added():
    items = []
    response = Mock()
    response.get_items = MagicMock(return_value=items)
    button = Mock()
    button.dict = MagicMock(return_value={'title': 'title', 'openUrlAction': 'url'})
    buttons = [button, button]
    image = Mock()
    image.dict = MagicMock(return_value={'url': 'url', 'accessibilityText': 'alt'})
    basic_card = BasicCard(title='title',
                           subtitle='subtitle',
                           text='text',
                           image=image,
                           buttons=buttons,
                           image_display_options='DEFAULT')
    basic_card.dict = MagicMock(return_value={'title': 'title',
                                              'subtitle': 'subtitle',
                                              'formattedText': 'text',
                                              'image': {'url': 'url', 'accessibilityText': 'alt'},
                                              'buttons': [{'title': 'title', 'openUrlAction': 'url'},
                                                          {'title': 'title', 'openUrlAction': 'url'}],
                                              'imageDisplayOptions': 'DEFAULT'})
    basic_card.add(response)
    assert items == [{'basicCard':
                     {'title': 'title',
                      'subtitle': 'subtitle',
                      'formattedText': 'text',
                      'image': {'url': 'url', 'accessibilityText': 'alt'},
                      'buttons': [{'title': 'title', 'openUrlAction': 'url'},
                                  {'title': 'title', 'openUrlAction': 'url'}],
                      'imageDisplayOptions': 'DEFAULT'}}]
