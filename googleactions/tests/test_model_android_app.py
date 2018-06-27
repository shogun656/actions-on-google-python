from googleactions import AndroidApp
from unittest.mock import Mock, MagicMock


def test_init():
    versions = [Mock()]
    android_app = AndroidApp(package_name='com.example.app', versions=versions)
    assert len(vars(android_app)) == 2
    assert android_app.package_name == 'com.example.app'
    assert android_app.versions == versions


def test_dict_is_equal():
    version = Mock()
    version.dict = MagicMock(return_value={'min_version': '1.0.0', 'maxVersion': '1.0.0'})
    android_app = AndroidApp(package_name='com.example.app', versions=version)
    assert android_app.dict() == {'packageName': 'com.example.app', 'versions':
                                  [{'min_version': '1.0.0', 'maxVersion': '1.0.0'}]}
