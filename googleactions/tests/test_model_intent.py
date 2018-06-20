from googleactions.models import Intent


def test_field_main():
    assert Intent.MAIN == 'actions.intent.MAIN'


def test_field_text():
    assert Intent.TEXT == 'actions.intent.TEXT'


def test_field_cancel():
    assert Intent.CANCEL == 'actions.intent.CANCEL'


def test_field_configure_updates():
    assert Intent.CONFIGURE_UPDATES == 'actions.intent.CONFIGURE_UPDATES'


def test_field_confirmation():
    assert Intent.CONFIRMATION == 'actions.intent.CONFIRMATION'


def test_field_datetime():
    assert Intent.DATETIME == 'actions.intent.DATETIME'


def test_field_delivery_address():
    assert Intent.DELIVERY_ADDRESS == 'actions.intent.DELIVERY_ADDRESS'


def test_field_new_surface():
    assert Intent.NEW_SURFACE == 'actions.intent.NEW_SURFACE'


def test_field_no_input():
    assert Intent.NO_INPUT == 'actions.intent.NO_INPUT'


def test_field_option():
    assert Intent.OPTION == 'actions.intent.OPTION'


def test_field_permission():
    assert Intent.PERMISSION == 'actions.intent.PERMISSION'


def test_field_sign_in():
    assert Intent.SIGN_IN == 'actions.intent.SIGN_IN'


def test_field_transaction_requirements_check():
    assert Intent.TRANSACTION_REQUIREMENTS_CHECK == 'actions.intent.TRANSACTION_REQUIREMENTS_CHECK'


def test_field_transaction_decision():
    assert Intent.TRANSACTION_DECISION == 'actions.intent.TRANSACTION_DECISION'


def test_register_update():
    assert Intent.REGISTER_UPDATE == 'actions.intent.REGISTER_UPDATE'


def test_place():
    assert Intent.PLACE == 'actions.intent.PLACE'


def test_link():
    assert Intent.LINK == 'actions.intent.LINK'


def test_fallback():
    assert Intent.FALLBACK == 'input.unknown'
