from googleactions import TableCard
from unittest.mock import Mock, MagicMock


def test_init():
    image = Mock()
    columns = [Mock()]
    rows = [Mock()]
    buttons = [Mock()]
    table_card = TableCard(title='title', subtitle='subtitle', image=image, columns=columns, rows=rows, buttons=buttons)
    assert len(vars(table_card)) == 6
    assert table_card.title == 'title'
    assert table_card.subtitle == 'subtitle'
    assert table_card.image == image
    assert table_card.column_properties == columns
    assert table_card.rows == rows
    assert table_card.buttons == buttons


def test_dict_is_equal():
    image = Mock()
    image.dict = MagicMock(return_value={'url': 'url'})
    column = Mock()
    column.dict = MagicMock(return_value={'header': 'header'})
    row = Mock()
    row.dict = MagicMock(return_value={'cells': [], 'dividerAfter': True})
    button = Mock()
    button.dict = MagicMock(return_value={'title': 'title'})
    table_card = TableCard(title='title', subtitle='subtitle', image=image, columns=column, rows=row, buttons=button)
    assert table_card.dict() == {'title': 'title',
                                 'subtitle': 'subtitle',
                                 'image': {'url': 'url'},
                                 'columnProperties': [{'header': 'header'}],
                                 'rows': [{'cells': [], 'dividerAfter': True}],
                                 'buttons': [{'title': 'title'}]}


def test_add_is_added():
    image = Mock()
    image.dict = MagicMock(return_value={'url': 'url'})
    column = Mock()
    column.dict = MagicMock(return_value={'header': 'header'})
    row = Mock()
    row.dict = MagicMock(return_value={'cells': [], 'dividerAfter': True})
    button = Mock()
    button.dict = MagicMock(return_value={'title': 'title'})
    table_card = TableCard(title='title', subtitle='subtitle', image=image, columns=column, rows=row, buttons=button)
    items = []
    response = Mock()
    response.get_items = MagicMock(return_value=items)
    table_card.dict = MagicMock(return_value={'title': 'title',
                                              'subtitle': 'subtitle',
                                              'image': {'url': 'url'},
                                              'columnProperties': [{'header': 'header'}],
                                              'rows': [{'cells': [], 'dividerAfter': True}],
                                              'buttons': [{'title': 'title'}]})
    table_card.add(response)
    assert items == [{'tableCard': {'title': 'title',
                                    'subtitle': 'subtitle',
                                    'image': {'url': 'url'},
                                    'columnProperties': [{'header': 'header'}],
                                    'rows': [{'cells': [], 'dividerAfter': True}],
                                    'buttons': [{'title': 'title'}]}}]
