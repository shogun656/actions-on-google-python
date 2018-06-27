from googleactions import HelperConfirmation, Helper
from unittest.mock import Mock, MagicMock


def setup_module(module):
    module.add_simple = Helper.add_simple


def teardown_module(module):
    Helper.add_simple = module.add_simple


def test_init():
    helper_confirmation = HelperConfirmation(question='question')
    assert len(vars(helper_confirmation)) == 1
    assert helper_confirmation.question == 'question'


def test_dict_is_equal():
    helper_confirmation = HelperConfirmation(question='question')
    assert helper_confirmation.dict() == {'intent': 'actions.intent.CONFIRMATION',
                                          'data': {'@type':
                                                   'type.googleapis.com/google.actions.v2.ConfirmationValueSpec',
                                                   'dialogSpec': {'requestConfirmationText': 'question'}}}


def test_add_is_added():
    helper_confirmation = HelperConfirmation(question='question')
    Helper.add_simple = MagicMock()
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    helper_confirmation.dict = MagicMock(return_value={'intent': 'actions.intent.CONFIRMATION',
                                                       'data': {'@type': ('type.googleapis.com/google.actions.v2.'
                                                                          'ConfirmationValueSpec'),
                                                                'dialogSpec': {'requestConfirmationText': 'question'}}})
    helper_confirmation.add(response)
    assert payload == {'systemIntent': {'intent': 'actions.intent.CONFIRMATION',
                                        'data': {'@type':
                                                 'type.googleapis.com/google.actions.v2.ConfirmationValueSpec',
                                                 'dialogSpec': {'requestConfirmationText': 'question'}}}}
    assert Helper.add_simple.call_count == 1
