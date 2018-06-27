from googleactions import Button


def test_init():
    button = Button(title='title', url='url')
    assert len(vars(button)) == 2
    assert button.title == 'title'
    assert button.open_url_action.url == 'url'


def test_dict_is_equal():
    button = Button(title='title', url='url')
    assert button.dict() == {'title': 'title', 'openUrlAction': {'url': 'url'}}
