from googleactions.utils import flatten
from unittest.mock import Mock


def test_flatten_not_list_string():
    flat = flatten('string')
    assert flat == ['string']


def test_flatten_not_list_object():
    obj = Mock()
    flat = flatten(obj)
    assert flat == [obj]


def test_flatten_list_strings():
    flat = flatten(['string1', 'string2'])
    assert flat == ['string1', 'string2']


def test_flatten_tuple_strings():
    flat = flatten(('string1', 'string2'))
    assert flat == ('string1', 'string2')


def test_flatten_list_objects():
    obj1 = Mock()
    obj2 = Mock()
    flat = flatten([obj1, obj2])
    assert flat == [obj1, obj2]


def test_flatten_tuple_objects():
    obj1 = Mock()
    obj2 = Mock()
    flat = flatten((obj1, obj2))
    assert flat == (obj1, obj2)


def test_flatten_nested_list_strings():
    flat = flatten(['1', ['2', ['3', ['4', ['5']]]], '6'])
    assert flat == ['1', '2', '3', '4', '5', '6']


def test_flatten_nested_tuples_strings():
    flat = flatten(('1', ('2', ('3', ('4', '5'))), '6'))
    assert flat == ('1', '2', '3', '4', '5', '6')


def test_flatten_nested_list_objects():
    obj1 = Mock()
    obj2 = Mock()
    obj3 = Mock()
    obj4 = Mock()
    obj5 = Mock()
    obj6 = Mock()
    flat = flatten([obj1, [obj2, [obj3, [obj4, [obj5]]]], obj6])
    assert flat == [obj1, obj2, obj3, obj4, obj5, obj6]


def test_flatten_nested_tuples_objects():
    obj1 = Mock()
    obj2 = Mock()
    obj3 = Mock()
    obj4 = Mock()
    obj5 = Mock()
    obj6 = Mock()
    flat = flatten((obj1, (obj2, (obj3, (obj4, obj5))), obj6))
    assert flat == (obj1, obj2, obj3, obj4, obj5, obj6)


def test_flatten_nested_tuples_lists():
    obj1 = Mock()
    obj2 = Mock()
    obj3 = Mock()
    obj4 = Mock()
    obj5 = Mock()
    obj6 = Mock()
    flat = flatten((obj1, [obj2, (obj3, [obj4, obj5])], obj6))
    assert flat == (obj1, obj2, obj3, obj4, obj5, obj6)


def test_flatten_nested_lists_tuples():
    obj1 = Mock()
    obj2 = Mock()
    obj3 = Mock()
    obj4 = Mock()
    obj5 = Mock()
    obj6 = Mock()
    flat = flatten([obj1, (obj2, [obj3, (obj4, obj5)]), obj6])
    assert flat == [obj1, obj2, obj3, obj4, obj5, obj6]


def test_flatten_nested_lists_tuples_mixed():
    obj1 = Mock()
    obj3 = Mock()
    obj4 = Mock()
    obj6 = Mock()
    flat = flatten([obj1, ('obj2', [obj3, (obj4, 5)]), obj6])
    assert flat == [obj1, 'obj2', obj3, obj4, 5, obj6]


def test_flatten_nested_tuples_lists_mixed():
    obj1 = Mock()
    obj3 = Mock()
    obj4 = Mock()
    obj6 = Mock()
    flat = flatten((obj1, ['obj2', (obj3, [obj4, 5])], obj6))
    assert flat == (obj1, 'obj2', obj3, obj4, 5, obj6)