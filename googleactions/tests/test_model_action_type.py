from googleactions.models import ActionType


def test_field_unknown_is_equal():
    assert ActionType.UNKNOWN == 'UNKNOWN'


def test_field_view_details_is_equal():
    assert ActionType.VIEW_DETAILS == 'VIEW_DETAILS'


def test_field_modify_is_equal():
    assert ActionType.MODIFY == 'MODIFY'


def test_field_cancel_is_equal():
    assert ActionType.CANCEL == 'CANCEL'


def test_field_return_is_equal():
    assert ActionType.RETURN == 'RETURN'


def test_field_exchange_is_equal():
    assert ActionType.EXCHANGE == 'EXCHANGE'


def test_field_email_is_equal():
    assert ActionType.EMAIL == 'EMAIL'


def test_field_call_is_equal():
    assert ActionType.CALL == 'CALL'


def test_field_reorder_is_equal():
    assert ActionType.REORDER == 'REORDER'


def test_field_review_is_equal():
    assert ActionType.REVIEW == 'REVIEW'


def test_field_customer_service_is_equal():
    assert ActionType.CUSTOMER_SERVICE == 'CUSTOMER_SERVICE'


def test_field_fix_issue_is_equal():
    assert ActionType.FIX_ISSUE == 'FIX_ISSUE'
