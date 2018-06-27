from googleactions import OpenUrlAction
from unittest.mock import Mock, MagicMock


def test_init():
    android_app = Mock()
    open_url_action = OpenUrlAction(url='url', android_app=android_app)
    assert len(vars(open_url_action)) == 2
    assert open_url_action.url == 'url'
    assert open_url_action.android_app == android_app


def test_dict_is_equal():
    android_app = Mock()
    android_app.dict = MagicMock(return_value={'packageName': 'com.app.example'})
    open_url_action = OpenUrlAction(url='url', android_app=android_app)
    assert open_url_action.dict() == {'url': 'url', 'androidApp': {'packageName': 'com.app.example'}}
