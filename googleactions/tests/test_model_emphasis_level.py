from googleactions.models import EmphasisLevel


def test_field_strong_is_equal():
    assert EmphasisLevel.STRONG == 'strong'


def test_field_moderate_is_equal():
    assert EmphasisLevel.MODERATE == 'moderate'


def test_field_none_is_equal():
    assert EmphasisLevel.NONE == 'none'


def test_field_reduced_is_equal():
    assert EmphasisLevel.REDUCED == 'reduced'
