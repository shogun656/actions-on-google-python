from googleactions import End
from unittest.mock import Mock, MagicMock


def test_init():
    end = End()
    assert len(vars(end)) == 0
    assert end is not None


def test_add_is_added():
    payload = {}
    response = Mock()
    response.get_google_payload = MagicMock(return_value=payload)
    end = End()
    end.add(response)
    assert payload == {'expectUserResponse': False}
