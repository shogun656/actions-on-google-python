from googleactions import HelperSignIn, Helper
from unittest.mock import Mock, MagicMock


def setup_module(module):
    module.add_simple = Helper.add_simple


def teardown_module(module):
    Helper.add_simple = module.add_simple


def test_init():
    helper_sign_in = HelperSignIn()
    assert len(vars(helper_sign_in)) == 0
    assert helper_sign_in is not None


def test_dict_is_equal():
    helper_sign_in = HelperSignIn()
    assert helper_sign_in.dict() == {'intent': 'actions.intent.SIGN_IN'}


def test_add_is_added():
    Helper.add_simple = MagicMock()
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    helper_sign_in = HelperSignIn()
    helper_sign_in.dict = MagicMock(return_value={'intent': 'actions.intent.SIGN_IN'})
    helper_sign_in.add(response)
    assert payload == {'systemIntent': {'intent': 'actions.intent.SIGN_IN'}}
    assert Helper.add_simple.call_count == 1
