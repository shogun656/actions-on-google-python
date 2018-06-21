from googleactions.models import ImageDisplayOptions


def test_field_default_is_equal():
    assert ImageDisplayOptions.DEFAULT == 'DEFAULT'


def test_field_white_is_equal():
    assert ImageDisplayOptions.WHITE == 'WHITE'


def test_field_cropped_is_equal():
    assert ImageDisplayOptions.CROPPED == 'CROPPED'
