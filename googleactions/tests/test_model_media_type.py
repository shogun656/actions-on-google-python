from googleactions.models import MediaType


def test_field_media_type_unspecified_is_equal():
    assert MediaType.MEDIA_TYPE_UNSPECIFIED == 'MEDIA_TYPE_UNSPECIFIED'


def test_field_audio_is_equal():
    MediaType.AUDIO == 'AUDIO'
