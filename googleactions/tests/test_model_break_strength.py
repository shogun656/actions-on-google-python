from googleactions.models import BreakStrength


def test_field_none_is_equal():
    assert BreakStrength.NONE == 'none'


def test_field_x_weak_is_equal():
    assert BreakStrength.X_WEAK == 'x-weak'


def test_field_weak_is_equal():
    assert BreakStrength.WEAK == 'weak'


def test_field_medium_is_equal():
    assert BreakStrength.MEDIUM == 'medium'


def test_field_strong_is_equal():
    assert BreakStrength.STRONG == 'strong'


def test_field_x_strong_is_equal():
    assert BreakStrength.X_STRONG == 'x-strong'
