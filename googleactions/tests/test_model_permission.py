from googleactions import Permission, Helper
from unittest.mock import Mock, MagicMock


def test_init():
    permissions = ['NAME', 'DEVICE_PRECISE_LOCATION']
    permission = Permission(context='context', permissions=permissions)
    assert len(vars(permission)) == 2
    assert permission.context == 'context'
    assert permission.permissions == permissions


def test_dict_is_equal():
    permission = Permission(context='context', permissions='NAME')
    assert permission.dict() == {'intent': 'actions.intent.PERMISSION',
                                 'data': {'@type': 'type.googleapis.com/google.actions.v2.PermissionValueSpec',
                                          'optContext': 'context',
                                          'permissions': ['NAME']}}


def test_add_is_added():
    Helper.add_simple = MagicMock()
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    permission = Permission(context='context', permissions='NAME')
    permission.dict = MagicMock(return_value={'intent': 'actions.intent.PERMISSION',
                                              'data': {'@type': ('type.googleapis.com/google.actions.v2.'
                                                                 'PermissionValueSpec'),
                                                       'optContext': 'context',
                                                       'permissions': ['NAME']}})
    permission.add(response)
    assert payload == {'systemIntent': {'intent': 'actions.intent.PERMISSION',
                                        'data': {'@type': 'type.googleapis.com/google.actions.v2.PermissionValueSpec',
                                                 'optContext': 'context',
                                                 'permissions': ['NAME']}}}
