from googleactions.models import AtType


def test_field_option_value_spec_is_equal():
    assert AtType.OPTION_VALUE_SPEC == 'type.googleapis.com/google.actions.v2.OptionValueSpec'


def test_field_permission_value_spec_is_equal():
    assert AtType.PERMISSION_VALUE_SPEC == 'type.googleapis.com/google.actions.v2.PermissionValueSpec'


def test_field_sign_in_value_is_equal():
    assert AtType.SIGN_IN_VALUE == 'type.googleapis.com/google.actions.v2.SignInValue'


def test_field_place_value_spec_is_equal():
    assert AtType.PLACE_VALUE_SPEC == 'type.googleapis.com/google.actions.v2.PlaceValueSpec'


def test_field_place_dialog_spec_is_equal():
    assert AtType.PLACE_DIALOG_SPEC == 'type.googleapis.com/google.actions.v2.PlaceValueSpec.PlaceDialogSpec'


def test_field_confirmation_value_spec_is_equal():
    assert AtType.CONFIRMATION_VALUE_SPEC == 'type.googleapis.com/google.actions.v2.ConfirmationValueSpec'


def test_field_link_value_spec_is_equal():
    assert AtType.LINK_VALUE_SPEC == 'type.googleapis.com/google.actions.v2.LinkValueSpec'


def test_field_new_surface_value_spec_is_equal():
    assert AtType.NEW_SURFACE_VALUE_SPEC == 'type.googleapis.com/google.actions.v2.NewSurfaceValueSpec'


def test_field_date_time_value_spec_is_equal():
    assert AtType.DATE_TIME_VALUE_SPEC == 'type.googleapis.com/google.actions.v2.DateTimeValueSpec'
