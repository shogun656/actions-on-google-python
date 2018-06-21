from googleactions.models import Capability


def test_field_screen_output_is_equal():
    assert Capability.SCREEN_OUTPUT == 'actions.capability.SCREEN_OUTPUT'


def test_field_audio_output_is_equal():
    assert Capability.AUDIO_OUTPUT == 'actions.capability.AUDIO_OUTPUT'


def test_field_media_response_audio_is_equal():
    assert Capability.MEDIA_RESPONSE_AUDIO == 'actions.capability.MEDIA_RESPONSE_AUDIO'


def test_field_web_browser_is_equal():
    assert Capability.WEB_BROWSER == 'actions.capability.WEB_BROWSER'
