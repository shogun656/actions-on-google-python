from googleactions.models import InterpretAs


def test_field_cardinal_is_equal():
    assert InterpretAs.CARDINAL == 'cardinal'


def test_field_ordinal_is_equal():
    assert InterpretAs.ORDINAL == 'ordinal'


def test_field_characters_is_equal():
    assert InterpretAs.CHARACTERS == 'characters'


def test_field_fraction_is_equal():
    assert InterpretAs.FRACTION == 'fraction'


def test_field_expletive_is_equal():
    assert InterpretAs.EXPLETIVE == 'expletive'


def test_field_bleep_is_equal():
    assert InterpretAs.BLEEP == 'bleep'


def test_field_unit_is_equal():
    assert InterpretAs.UNIT == 'unit'


def test_field_verbatim_is_equal():
    assert InterpretAs.VERBATIM == 'verbatim'


def test_field_spell_out_is_equal():
    assert InterpretAs.SPELL_OUT == 'spell-out'


def test_field_date_is_equal():
    assert InterpretAs.DATE == 'date'


def test_field_time_is_equal():
    assert InterpretAs.TIME == 'time'


def test_field_telephone_is_equal():
    assert InterpretAs.TELEPHONE == 'telephone'
