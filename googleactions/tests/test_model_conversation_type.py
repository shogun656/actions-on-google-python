from googleactions.models import ConversationType


def test_field_type_unspecified_is_equal():
    assert ConversationType.TYPE_UNSPECIFIED == 'TYPE_UNSPECIFIED'


def test_field_new_is_equal():
    assert ConversationType.NEW == 'NEW'


def test_field_active_is_equal():
    assert ConversationType.ACTIVE == 'ACTIVE'
