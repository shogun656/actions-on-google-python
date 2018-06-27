from googleactions import TimeOfDay


def test_init():
    time_of_day = TimeOfDay(hours=0, minutes=1, seconds=60, nanos=100)
    assert len(vars(time_of_day)) == 4
    assert time_of_day.hours == 0
    assert time_of_day.minutes == 1
    assert time_of_day.seconds == 60
    assert time_of_day.nanos == 100
