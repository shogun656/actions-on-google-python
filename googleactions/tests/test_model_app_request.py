from googleactions import AppRequest
from unittest.mock import Mock, MagicMock


def setup_module(module):
    module.check_surface = AppRequest.check_surface
    global MODULE
    MODULE = module


def teardown_module(module):
    AppRequest.check_surface = module.check_surface


def test_init():
    app_request = AppRequest(data={'inputs': {'rawInputs': [], 'intent': 'actions.intent.MAIN'}}, as_json=False)
    assert app_request.data == {'inputs': {'rawInputs': [], 'intent': 'actions.intent.MAIN'}}


def test_init_json():
    app_request = AppRequest(data='{"inputs": {"rawInputs": [], "intent": "actions.intent.MAIN"}}', as_json=True)
    assert app_request.data == {'inputs': {'rawInputs': [], 'intent': 'actions.intent.MAIN'}}


def test_get_payload():
    payload = {}
    app_request = AppRequest(data={'originalDetectIntentRequest': {'payload': payload}}, as_json=False)
    assert app_request.get_payload() == payload


def test_get_query():
    query = 'query'
    app_request = AppRequest(data={'queryResult': {'queryText': query}}, as_json=False)
    assert app_request.get_query() == query


def test_get_data():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_storage = MagicMock(return_value={'key': 'value'})
    app_request.get_param = MagicMock(return_value='value')
    assert app_request.get_data('key') == 'value'


def test_get_data_storage_only():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_storage = MagicMock(return_value={'key': 'value'})
    assert app_request.get_data('key') == 'value'


def test_get_data_param_only():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_param = MagicMock(return_value='value')
    assert app_request.get_data('key') == 'value'


def test_get_data_diff_keys_storage():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_storage = MagicMock(return_value={'key_a': 'value'})
    assert app_request.get_data(storage_name='key_a', param_name='key_b') == 'value'


def test_get_data_diff_keys_param():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_param = MagicMock(return_value='value')
    assert app_request.get_data(storage_name='key_a', param_name='key_b') == 'value'


def test_get_data_is_none():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_storage = MagicMock(return_value={})
    app_request.get_param = MagicMock(return_value=None)
    assert app_request.get_data('key') is None


def test_get_params():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_query_result = MagicMock(return_value={'outputContexts':
                                                           [{'parameters': {'key_a': 'value_a',
                                                                            'key_a.original': 'ValueA'}},
                                                            {'parameters': {'key_b': 'value_b',
                                                                            'key_b.original': 'ValueB'}}]})
    return app_request.get_params() == [{'parameters': {'key_a': 'value_a',
                                                        'key_a.original': 'ValueA'}},
                                        {'parameters': {'key_b': 'value_b',
                                                        'key_b.original': 'ValueB'}}]


def test_get_param():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_params = MagicMock(return_value=[{'key_a': 'value_a', 'key_a.original': 'ValueA'},
                                                     {'key_b': 'value_b', 'key_b.original': 'ValueB'}])
    assert app_request.get_param('key_b') == 'value_b'


def test_get_param_is_original():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_params = MagicMock(return_value=[{'key_a': 'value_a', 'key_a.original': 'ValueA'},
                                                     {'key_b': 'value_b', 'key_b.original': 'ValueB'}])
    assert app_request.get_param('key_b', original=True) == 'ValueB'


def test_get_param_is_none():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_params = MagicMock(return_value=[{'key_a': 'value_a', 'key_a.original': 'ValueA'},
                                                     {'key_b': 'value_b', 'key_b.original': 'ValueB'}])
    assert app_request.get_param('key_c') is None


def test_has_all_params():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_query_result = MagicMock(return_value={'allRequiredParamsPresent': True})
    assert app_request.has_all_params() is True


def test_has_all_params_false():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_query_result = MagicMock(return_value={'allRequiredParamsPresent': False})
    assert app_request.has_all_params() is False


def test_has_all_params_none():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_query_result = MagicMock(return_value={})
    assert app_request.has_all_params() is False


def test_has():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_payload = MagicMock(return_value={'surface': {}})
    AppRequest.check_surface = MagicMock(return_value=True)
    assert app_request.has(capabilities='actions.capability.SCREEN_OUTPUT') is True
    assert app_request.get_payload.call_count == 1
    assert AppRequest.check_surface.call_count == 1


def test_has_is_none():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_payload = MagicMock(return_value={})
    AppRequest.check_surface = MagicMock(return_value=True)
    assert app_request.has(capabilities='actions.capability.SCREEN_OUTPUT') is False


def test_has_surface_false():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_payload = MagicMock(return_value={'availableSurfaces': [{}, {}]})
    AppRequest.check_surface = MagicMock(return_value=False)
    assert app_request.has_surface(capabilities='actions.capability.SCREEN_OUTPUT') is False
    assert AppRequest.check_surface.call_count == 2


def test_has_surface_false():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_payload = MagicMock(return_value={'availableSurfaces': [{}, {}]})
    AppRequest.check_surface = MagicMock(return_value=True)
    assert app_request.has_surface(capabilities='actions.capability.SCREEN_OUTPUT') is True
    assert AppRequest.check_surface.call_count == 1


def test_has_surface_no_surfaces():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_payload = MagicMock(return_value={})
    AppRequest.check_surface = MagicMock(return_value=True)
    assert app_request.has_surface(capabilities='actions.capability.SCREEN_OUTPUT') is False
    assert AppRequest.check_surface.call_count == 0


def test_is_intent_true_event_name():
    app_request = AppRequest(data={}, as_json=False)
    app_request.is_dialogflow_event_name = MagicMock(return_value=True)
    app_request.is_dialogflow_action = MagicMock(return_value=False)
    app_request.get_input = MagicMock(return_value=None)
    assert app_request.is_intent('intent') is True


def test_is_intent_true_action():
    app_request = AppRequest(data={}, as_json=False)
    app_request.is_dialogflow_event_name = MagicMock(return_value=False)
    app_request.is_dialogflow_action = MagicMock(return_value=True)
    app_request.get_input = MagicMock(return_value=None)
    assert app_request.is_intent('intent') is True


def test_is_intent_true_get_input():
    app_request = AppRequest(data={}, as_json=False)
    app_request.is_dialogflow_event_name = MagicMock(return_value=False)
    app_request.is_dialogflow_action = MagicMock(return_value=True)
    app_request.get_input = MagicMock(return_value=None)
    assert app_request.is_intent('intent') is True


def test_get_input():
    app_request = AppRequest(data={}, as_json=False)
    input = {'intent': 'actions.intent.MAIN'}
    app_request.get_payload = MagicMock(return_value={'inputs': [input]})
    assert app_request.get_input('actions.intent.MAIN') == input


def test_is_dialogflow_event_name_is_true():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_query_result = MagicMock(return_value={'intent': {'displayName': 'name'}})
    assert app_request.is_dialogflow_event_name('name') is True


def test_is_dialogflow_event_name_is_false():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_query_result = MagicMock(return_value={'intent': {'displayName': 'name'}})
    assert app_request.is_dialogflow_event_name('other_name') is False


def test_is_dialogflow_is_action_is_true():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_query_result = MagicMock(return_value={'action': 'action'})
    assert app_request.is_dialogflow_action('action') is True


def test_is_dialogflow_is_action_is_false():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_query_result = MagicMock(return_value={'action': 'action'})
    assert app_request.is_dialogflow_action('other_action') is False


def test_get_selected_option():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_input = MagicMock(return_value={'arguments': [{'textValue': 'text'}]})
    assert app_request.get_selected_option() == 'text'


def test_get_selected_option_is_none():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_input = MagicMock(return_value=None)
    assert app_request.get_selected_option() is None


def test_get_helper_date_time():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_input = MagicMock(return_value={'arguments':
                                                    [{'datetimeValue': {
                                                        'date': {'year': '2018',
                                                                 'month': '2',
                                                                 'day': '3'},
                                                        'time': {'hours': '4',
                                                                 'minutes': '30',
                                                                 'seconds': '10',
                                                                 'nanos': '20'}}}]})
    datetime = app_request.get_helper_date_time()
    date = datetime.date
    time = datetime.time
    assert date.year == '2018'
    assert date.month == '2'
    assert date.day == '3'
    assert time.hours == '4'
    assert time.minutes == '30'
    assert time.seconds == '10'
    assert time.nanos == '20'


def test_get_helper_date_time_is_none():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_input = MagicMock(return_value=None)
    assert app_request.get_helper_date_time() is None


def test_has_permission_text_value():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_input = MagicMock(return_value={'arguments': [{'textValue': 'true'}]})
    assert app_request.has_permission() is True


def test_has_permission_bool_value():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_input = MagicMock(return_value={'arguments': [{'boolValue': True}]})
    assert app_request.has_permission() is True


def test_has_permission_bool_value():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_input = MagicMock(return_value={'arguments': [{}]})
    assert app_request.has_permission() is False


def test_has_permission_bool_value():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_input = MagicMock(return_value=None)
    assert app_request.has_permission() is False


def test_get_permission_user_profile():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_payload = MagicMock(return_value={'user':
                                                      {'profile':
                                                       {'displayName': 'Chet F.',
                                                        'givenName': 'Chet',
                                                        'familyName': 'Forte'}}})
    user_profile = app_request.get_permission_user_profile()
    assert user_profile.display_name == 'Chet F.'
    assert user_profile.given_name == 'Chet'
    assert user_profile.family_name == 'Forte'


def test_get_permission_location():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_payload = MagicMock(return_value={'device':
                                                      {'location':
                                                       {'coordinates':
                                                        {'latitude': 34.01,
                                                         'longitude': -86.44}}}})
    lat_lng = app_request.get_permission_location()
    assert lat_lng.latitude == 34.01
    assert lat_lng.longitude == -86.44


def test_is_helper_signed_in_is_true():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_input = MagicMock(return_value={'arguments': [{'extension': {'status': 'OK'}}]})
    assert app_request.is_helper_signed_in() is True


def test_is_helper_signed_in_is_false():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_input = MagicMock(return_value={'arguments': [{'extension': {'status': 'NO'}}]})
    assert app_request.is_helper_signed_in() is False


def test_is_helper_signed_in_is_false_no_input():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_input = MagicMock(return_value=None)
    assert app_request.is_helper_signed_in() is False


def test_get_helper_sign_in_access_token():
    app_request = AppRequest(data={}, as_json=False)
    user = Mock()
    user.accessToken = '123'
    app_request.get_user = MagicMock(return_value=user)
    assert app_request.get_helper_sign_in_access_token() == '123'


def test_get_helper_place():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_input = MagicMock(return_value={'arguments':
                                                    [{'placeValue':
                                                      {'coordinates':
                                                       {'latitude': 34.01,
                                                        'longitude': -86.44},
                                                       'name': 'name',
                                                       'formattedAddress': '1234 Silver Ln',
                                                       'placeId': '2312-#12412'}}]})
    location = app_request.get_helper_place()
    coordinates = location.coordinates
    assert coordinates.latitude == 34.01
    assert coordinates.longitude == -86.44
    assert location.name == 'name'
    assert location.formatted_address == '1234 Silver Ln'
    assert location.place_id == '2312-#12412'


def test_get_helper_confirmation():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_input = MagicMock(return_value={'arguments': [{'boolValue': True}]})
    assert app_request.get_helper_confirmation() is True


def test_get_helper_link_status():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_input = MagicMock(return_value={'arguments': [{'status': {'code': '1'}}]})
    assert app_request.get_helper_link_status() == '1'


def test_get_helper_new_surface():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_input = MagicMock(return_value={'arguments': [{'extension': {'status': 'OK'}}]})
    assert app_request.get_helper_new_surface() is True


def test_get_storage():
    app_request = AppRequest(data={}, as_json=False)
    app_request.get_payload = MagicMock(return_value={'user':
                                                      {'userStorage':
                                                       '{"key1": "value1", "key2": "value2"}'}})
    assert app_request.get_storage() == {'key1': 'value1', 'key2': 'value2'}


def test_check_surface_one_is_true():
    AppRequest.check_surface = MODULE.check_surface
    assert AppRequest.check_surface({'capabilities': [{'name': 'actions.capability.SCREEN_OUTPUT'}]},
                                    'actions.capability.SCREEN_OUTPUT') is True


def test_check_surface_two_is_true():
    AppRequest.check_surface = MODULE.check_surface
    assert AppRequest.check_surface({'capabilities': [{'name': 'actions.capability.SCREEN_OUTPUT'},
                                                      {'name': 'actions.capability.AUDIO_OUTPUT'}]},
                                    ['actions.capability.SCREEN_OUTPUT',
                                     'actions.capability.AUDIO_OUTPUT']) is True


def test_check_surface_is_true_subset():
    AppRequest.check_surface = MODULE.check_surface
    assert AppRequest.check_surface({'capabilities': [{'name': 'actions.capability.SCREEN_OUTPUT'},
                                                      {'name': 'actions.capability.AUDIO_OUTPUT'}]},
                                    ['actions.capability.SCREEN_OUTPUT']) is True


def test_check_surface_is_false_subset():
    AppRequest.check_surface = MODULE.check_surface
    assert AppRequest.check_surface({'capabilities': [{'name': 'actions.capability.SCREEN_OUTPUT'}]},
                                    ['actions.capability.SCREEN_OUTPUT',
                                     'actions.capability.AUDIO_OUTPUT']) is False


def test_json():
    app_request = AppRequest(data={'key1': 'value1', 'key2': 'value2', 'key3': ['a', 'b', 'c']}, as_json=False)
    assert app_request.json() == '{"key1": "value1", "key2": "value2", "key3": ["a", "b", "c"]}'
