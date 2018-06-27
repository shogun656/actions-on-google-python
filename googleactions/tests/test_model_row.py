from googleactions import Row
from unittest.mock import Mock, MagicMock


def test_init():
    cells = [Mock()]
    row = Row(cells=cells, divider_after=True)
    assert len(vars(row)) == 2
    assert row.cells == cells
    assert row.divider_after is True


def test_dict_is_equal():
    cell = Mock()
    cell.dict = MagicMock(return_value={'text': 'text'})
    row = Row(cells=cell, divider_after=False)
    assert row.dict() == {'cells': [{'text': 'text'}], 'dividerAfter': False}
