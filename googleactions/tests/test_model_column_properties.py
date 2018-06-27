from googleactions import ColumnProperties


def test_init():
    column_properties = ColumnProperties(header='header', align='CENTER')
    assert len(vars(column_properties)) == 2
    assert column_properties.header == 'header'
    assert column_properties.horizontal_alignment == 'CENTER'


def test_dict_is_equal():
    column_properties = ColumnProperties(header='header', align='CENTER')
    assert column_properties.dict() == {'header': 'header', 'horizontalAlignment': 'CENTER'}
