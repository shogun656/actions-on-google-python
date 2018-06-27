from googleactions import DateTime
from unittest.mock import Mock


def test_init():
    date = Mock()
    time = Mock()
    date_time = DateTime(date=date, time=time)
    assert len(vars(date_time)) == 2
    assert date_time.date == date
    assert date_time.time == time
