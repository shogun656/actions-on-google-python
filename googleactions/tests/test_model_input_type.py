from googleactions.models import InputType


def test_field_unspecified_input_type_is_equal():
    assert InputType.UNSPECIFIED_INPUT_TYPE == 'UNSPECIFIED_INPUT_TYPE'


def test_field_touch_is_equal():
    assert InputType.TOUCH == 'TOUCH'


def test_field_voice_is_equal():
    assert InputType.VOICE == 'VOICE'


def test_field_keyboard_is_equal():
    assert InputType.KEYBOARD == 'KEYBOARD'
