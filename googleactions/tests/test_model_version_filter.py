from googleactions import VersionFilter


def test_init():
    version_filter = VersionFilter(min_version='1.0.0', max_version='2.0.0')
    assert len(vars(version_filter)) == 2
    assert version_filter.min_version == '1.0.0'
    assert version_filter.max_version == '2.0.0'


def test_dict_is_equal():
    version_filter = VersionFilter(min_version='1.0.0', max_version='2.0.0')
    assert version_filter.dict() == {'minVersion': '1.0.0', 'maxVersion': '2.0.0'}


def test_dict_is_equal_min():
    version_filter = VersionFilter(min_version='1.0.0')
    assert version_filter.dict() == {'minVersion': '1.0.0'}


def test_dict_is_equal_max():
    version_filter = VersionFilter(max_version='2.0.0')
    assert version_filter.dict() == {'maxVersion': '2.0.0'}
