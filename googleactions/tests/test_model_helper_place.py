from googleactions import HelperPlace, Helper
from unittest.mock import Mock, MagicMock


def setup_module(module):
    module.add_simple = Helper.add_simple


def teardown_module(module):
    Helper.add_simple = module.add_simple


def test_init():
    helper_place = HelperPlace(prompt='prompt', context='context')
    assert len(vars(helper_place)) == 2
    assert helper_place.prompt == 'prompt'
    assert helper_place.context == 'context'


def test_dict_is_equal():
    helper_place = HelperPlace(prompt='prompt', context='context')
    assert helper_place.dict() == {'intent': 'actions.intent.PLACE',
                                   'data': {'@type': 'type.googleapis.com/google.actions.v2.PlaceValueSpec',
                                            'dialogSpec': {
                                                'extension': {
                                                    '@type': ('type.googleapis.com/google.actions.v2'
                                                              '.PlaceValueSpec.PlaceDialogSpec'),
                                                    'requestPrompt': 'prompt',
                                                    'permissionContext': 'context'}}}}


def test_add_is_added():
    helper_place = HelperPlace(prompt='prompt', context='context')
    Helper.add_simple = MagicMock()
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    helper_place.dict = MagicMock(return_value={'intent': 'actions.intent.PLACE',
                                                'data': {'@type': ('type.googleapis.com/google.actions.v2.'
                                                                   'PlaceValueSpec'),
                                                         'dialogSpec': {
                                                             'extension': {
                                                                 '@type': ('type.googleapis.com/google.actions.v2'
                                                                           '.PlaceValueSpec.PlaceDialogSpec'),
                                                                 'requestPrompt': 'prompt',
                                                                 'permissionContext': 'context'}}}})
    helper_place.add(response)
    assert payload == {'systemIntent': {'intent': 'actions.intent.PLACE',
                                        'data': {'@type': 'type.googleapis.com/google.actions.v2.PlaceValueSpec',
                                                 'dialogSpec': {
                                                     'extension': {
                                                         '@type': ('type.googleapis.com/google.actions.v2'
                                                                   '.PlaceValueSpec.PlaceDialogSpec'),
                                                         'requestPrompt': 'prompt',
                                                         'permissionContext': 'context'}}}}}
    assert Helper.add_simple.call_count == 1
