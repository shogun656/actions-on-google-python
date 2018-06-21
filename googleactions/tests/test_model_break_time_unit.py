from googleactions.models import BreakTimeUnit


def test_field_millis_is_equal():
    assert BreakTimeUnit.MILLIS == 'ms'


def test_field_seconds_is_equal():
    assert BreakTimeUnit.SECONDS == 's'
