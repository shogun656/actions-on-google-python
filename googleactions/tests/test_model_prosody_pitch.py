from googleactions.models import ProsodyPitch


def test_field_x_low_is_equal():
    assert ProsodyPitch.X_LOW == 'x-low'


def test_field_low_is_equal():
    assert ProsodyPitch.LOW == 'low'


def test_field_medium_is_equal():
    assert ProsodyPitch.MEDIUM == 'medium'


def test_field_high_is_equal():
    assert ProsodyPitch.HIGH == 'high'


def test_field_x_high_is_equal():
    assert ProsodyPitch.X_HIGH == 'x-high'


def test_field_default_is_equal():
    assert ProsodyPitch.DEFAULT == 'default'
