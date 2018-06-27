from googleactions import HelperAndroidLink, Helper
from unittest.mock import Mock, MagicMock


def setup_module(module):
    module.add_simple = Helper.add_simple


def teardown_module(module):
    Helper.add_simple = module.add_simple


def test_init():
    helper_android_link = HelperAndroidLink(url='url', package='com.app.example', reason='reason')
    open_url_action = helper_android_link.open_url_action
    android_app = open_url_action.android_app
    assert len(vars(helper_android_link)) == 2
    assert open_url_action.url == 'url'
    assert android_app.package_name == 'com.app.example'
    assert helper_android_link.reason == 'reason'


def test_dict_is_equal():
    helper_android_link = HelperAndroidLink(url='url', package='com.app.example', reason='reason')
    assert helper_android_link.dict() == {'intent': 'actions.intent.LINK',
                                          'data': {'@type': 'type.googleapis.com/google.actions.v2.LinkValueSpec',
                                                   'openUrlAction': {'url': 'url',
                                                                     'androidApp': {'packageName': 'com.app.example'}},
                                                   'dialogSpec': {
                                                       'requestLinkReason': 'reason'}}}


def test_add_is_added():
    helper_android_link = HelperAndroidLink(url='url', package='com.app.example', reason='reason')
    Helper.add_simple = MagicMock()
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    helper_android_link.dict = MagicMock(return_value={'intent': 'actions.intent.LINK',
                                                       'data': {'@type': ('type.googleapis.com/google.actions.v2.'
                                                                          'LinkValueSpec'),
                                                                'openUrlAction': {'url': 'url',
                                                                                  'androidApp':
                                                                                  {'packageName': 'com.app.example'}},
                                                                'dialogSpec': {
                                                                    'requestLinkReason': 'reason'}}})
    helper_android_link.add(response)
    assert payload == {'systemIntent': {'intent': 'actions.intent.LINK',
                                        'data': {'@type': 'type.googleapis.com/google.actions.v2.LinkValueSpec',
                                                 'openUrlAction': {'url': 'url',
                                                                   'androidApp': {'packageName': 'com.app.example'}},
                                                 'dialogSpec': {
                                                     'requestLinkReason': 'reason'}}}}
    assert Helper.add_simple.call_count == 1
