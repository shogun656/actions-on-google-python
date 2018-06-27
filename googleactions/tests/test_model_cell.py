from googleactions import Cell


def test_init():
    cell = Cell(text='text')
    assert len(vars(cell)) == 1
    assert cell.text == 'text'


def test_dict_is_equal():
    cell = Cell(text='text')
    assert cell.dict() == {'text': 'text'}
