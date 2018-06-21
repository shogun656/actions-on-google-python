from googleactions.models import ProsodyRate


def test_field_x_slow_is_equal():
    assert ProsodyRate.X_SLOW == "x-slow"


def test_field_slow_is_equal():
    assert ProsodyRate.SLOW == "slow"


def test_field_medium_is_equal():
    assert ProsodyRate.MEDIUM == "medium"


def test_field_fast_is_equal():
    assert ProsodyRate.FAST == "fast"


def test_field_x_fast_is_equal():
    assert ProsodyRate.X_FAST == "x-fast"


def test_field_default_is_equal():
    assert ProsodyRate.DEFAULT == "default"
