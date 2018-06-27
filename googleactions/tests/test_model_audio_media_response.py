from googleactions import AudioMediaResponse
from unittest.mock import Mock


def test_init():
    icon = Mock()
    large_image = Mock()
    audio_media_response = AudioMediaResponse(name='name', description='description', url='url',
                                              icon=icon, large_image=large_image)
    media_object = audio_media_response.media_objects[0]
    assert len(vars(media_object)) == 5
    assert media_object.name == 'name'
    assert media_object.description == 'description'
    assert media_object.content_url == 'url'
    assert media_object.icon == icon
    assert media_object.large_image == large_image
    assert audio_media_response.media_type == 'AUDIO'
