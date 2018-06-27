from googleactions import HelperDateTime, Helper
from unittest.mock import Mock, MagicMock


def setup_module(module):
    module.add_simple = Helper.add_simple


def teardown_module(module):
    Helper.add_simple = module.add_simple


def test_init():
    helper_date_time = HelperDateTime(date_time_text='date_time', date_text='date', time_text='time')
    assert len(vars(helper_date_time)) == 3
    assert helper_date_time.date_time_text == 'date_time'
    assert helper_date_time.date_text == 'date'
    assert helper_date_time.time_text == 'time'


def test_dict_is_equal():
    helper_date_time = HelperDateTime(date_time_text='date_time', date_text='date', time_text='time')
    assert helper_date_time.dict() == {'intent': 'actions.intent.DATETIME',
                                       'data': {'@type': 'type.googleapis.com/google.actions.v2.DateTimeValueSpec',
                                                'dialogSpec': {
                                                    'requestDatetimeText': 'date_time',
                                                    'requestDateText': 'date',
                                                    'requestTimeText': 'time'}}}


def test_add_is_added():
    helper_date_time = HelperDateTime(date_time_text='date_time', date_text='date', time_text='time')
    Helper.add_simple = MagicMock()
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    helper_date_time.dict = MagicMock(return_value={'intent': 'actions.intent.DATETIME',
                                                    'data': {'@type': ('type.googleapis.com/google.actions.v2.'
                                                                       'DateTimeValueSpec'),
                                                             'dialogSpec': {
                                                                 'requestDatetimeText': 'date_time',
                                                                 'requestDateText': 'date',
                                                                 'requestTimeText': 'time'}}})
    helper_date_time.add(response)
    assert payload == {'systemIntent': {'intent': 'actions.intent.DATETIME',
                                        'data': {'@type': 'type.googleapis.com/google.actions.v2.DateTimeValueSpec',
                                                 'dialogSpec': {
                                                     'requestDatetimeText': 'date_time',
                                                     'requestDateText': 'date',
                                                     'requestTimeText': 'time'}}}}
    assert Helper.add_simple.call_count == 1
