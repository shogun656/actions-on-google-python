from googleactions.models import Intent


def test_field_main_is_equal():
    assert Intent.MAIN == 'actions.intent.MAIN'


def test_field_text_is_equal():
    assert Intent.TEXT == 'actions.intent.TEXT'


def test_field_cancel_is_equal():
    assert Intent.CANCEL == 'actions.intent.CANCEL'


def test_field_configure_updates_is_equal():
    assert Intent.CONFIGURE_UPDATES == 'actions.intent.CONFIGURE_UPDATES'


def test_field_confirmation_is_equal():
    assert Intent.CONFIRMATION == 'actions.intent.CONFIRMATION'


def test_field_datetime_is_equal():
    assert Intent.DATETIME == 'actions.intent.DATETIME'


def test_field_delivery_address_is_equal():
    assert Intent.DELIVERY_ADDRESS == 'actions.intent.DELIVERY_ADDRESS'


def test_field_new_surface_is_equal():
    assert Intent.NEW_SURFACE == 'actions.intent.NEW_SURFACE'


def test_field_no_input_is_equal():
    assert Intent.NO_INPUT == 'actions.intent.NO_INPUT'


def test_field_option_is_equal():
    assert Intent.OPTION == 'actions.intent.OPTION'


def test_field_permission_is_equal():
    assert Intent.PERMISSION == 'actions.intent.PERMISSION'


def test_field_sign_in_is_equal():
    assert Intent.SIGN_IN == 'actions.intent.SIGN_IN'


def test_field_transaction_requirements_check_is_equal():
    assert Intent.TRANSACTION_REQUIREMENTS_CHECK == 'actions.intent.TRANSACTION_REQUIREMENTS_CHECK'


def test_field_transaction_decision_is_equal():
    assert Intent.TRANSACTION_DECISION == 'actions.intent.TRANSACTION_DECISION'


def test_register_update_is_equal():
    assert Intent.REGISTER_UPDATE == 'actions.intent.REGISTER_UPDATE'


def test_place_is_equal():
    assert Intent.PLACE == 'actions.intent.PLACE'


def test_link_is_equal():
    assert Intent.LINK == 'actions.intent.LINK'


def test_fallback_is_equal():
    assert Intent.FALLBACK == 'input.unknown'
