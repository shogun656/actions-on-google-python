from googleactions import LatLng


def test_init():
    latlng = LatLng(latitude=89.0, longitude=43.0)
    assert len(vars(latlng)) == 2
    assert latlng.latitude == 89.0
    assert latlng.longitude == 43.0
