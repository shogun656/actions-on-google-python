from googleactions.models import PermissionType


def test_field_name_is_equal():
    assert PermissionType.NAME == 'NAME'


def test_field_location_is_equal():
    assert PermissionType.LOCATION == 'DEVICE_PRECISE_LOCATION'


def test_field_unspecified_permission_is_equal():
    assert PermissionType.UNSPECIFIED_PERMISSION == 'UNSPECIFIED_PERMISSION'


def test_field_device_corase_location_is_equal():
    assert PermissionType.DEVICE_COARSE_LOCATION == 'DEVICE_COARSE_LOCATION'


def test_field_update_is_equal():
    assert PermissionType.UPDATE == 'UPDATE'
