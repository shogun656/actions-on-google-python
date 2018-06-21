from googleactions.models import UrlTypeHint


def test_field_url_type_hint_unspecified_is_equal():
    assert UrlTypeHint.URL_TYPE_HINT_UNSPECIFIED == 'URL_TYPE_HINT_UNSPECIFIED'


def test_field_amp_content_is_equal():
    assert UrlTypeHint.AMP_CONTENT == 'AMP_CONTENT'
