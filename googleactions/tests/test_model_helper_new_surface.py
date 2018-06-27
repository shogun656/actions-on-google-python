from googleactions import HelperNewSurface, Helper
from unittest.mock import Mock, MagicMock


def setup_module(module):
    module.add_simple = Helper.add_simple


def teardown_module(module):
    Helper.add_simple = module.add_simple


def test_init():
    capabilities = ['actions.capability.SCREEN_OUTPUT']
    helper_new_surface = HelperNewSurface(context='context',
                                          notification_title='notification',
                                          capabilities=capabilities)
    assert len(vars(helper_new_surface)) == 3
    assert helper_new_surface.context == 'context'
    assert helper_new_surface.notification_title == 'notification'
    assert helper_new_surface.capabilities == capabilities


def test_dict_is_equal():
    helper_new_surface = HelperNewSurface(context='context',
                                          notification_title='notification',
                                          capabilities='actions.capability.SCREEN_OUTPUT')
    assert helper_new_surface.dict() == {'intent': 'actions.intent.NEW_SURFACE',
                                         'data': {'@type': 'type.googleapis.com/google.actions.v2.NewSurfaceValueSpec',
                                                  'context': 'context',
                                                  'notificationTitle': 'notification',
                                                  'capabilities': ['actions.capability.SCREEN_OUTPUT']}}


def test_add_is_added():
    helper_new_surface = HelperNewSurface(context='context',
                                          notification_title='notification',
                                          capabilities='actions.capability.SCREEN_OUTPUT')
    Helper.add_simple = MagicMock()
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    helper_new_surface.dict = MagicMock(return_value={'intent': 'actions.intent.NEW_SURFACE',
                                                      'data': {'@type': ('type.googleapis.com/google.actions.v2.'
                                                                         'NewSurfaceValueSpec'),
                                                               'context': 'context',
                                                               'notificationTitle': 'notification',
                                                               'capabilities': ['actions.capability.SCREEN_OUTPUT']}})
    helper_new_surface.add(response)
    assert payload == {'systemIntent': {'intent': 'actions.intent.NEW_SURFACE',
                                        'data': {'@type': 'type.googleapis.com/google.actions.v2.NewSurfaceValueSpec',
                                                 'context': 'context',
                                                 'notificationTitle': 'notification',
                                                 'capabilities': ['actions.capability.SCREEN_OUTPUT']}}}
    assert Helper.add_simple.call_count == 1
