from googleactions import Location
from unittest.mock import Mock


def test_init():
    coordinates = Mock()
    location = Location(coordinates=coordinates, name='name', formatted_address='1234 abc ln', place_id='ff34j')
    assert len(vars(location)) == 4
    assert location.coordinates == coordinates
    assert location.name == 'name'
    assert location.formatted_address == '1234 abc ln'
    assert location.place_id == 'ff34j'
