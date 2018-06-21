from googleactions.models import HorizontalAlignment


def test_field_name_is_equal():
    assert HorizontalAlignment.LEADING == 'LEADING'


def test_field_name_is_equal():
    assert HorizontalAlignment.CENTER == 'CENTER'


def test_field_name_is_equal():
    assert HorizontalAlignment.TRAILING == 'TRAILING'
