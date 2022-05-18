import pytest
from repair_cost import calculate_total, calculate_amount_to_be_paid


# Unit test
def test_accessibility_of_calculate_total():
    try:
        _ = calculate_total([])
        assert True
    except (NameError, AssertionError):
        assert False


# Unit test
def test_calculate_total_with_empty_list():
        total = calculate_total(values=[])
        assert total == 0


# Unit test
def test_calculate_total_with_incorrect_argument_type():
    with pytest.raises(ValueError):
        _ = calculate_total(values=20)
        assert False
    assert True


# Unit test
def test_calculate_total_with_non_integral_list_values():
    with pytest.raises(ValueError):
        _ = calculate_total(values=['a', 10, 5.2])
        assert False
    assert True


# Unit test
def test_calculate_total_with_list_with_integral_values():
        total = calculate_total(values=[1000, 800, 200])
        assert total == 2000


# Unit test
def test_accessibility_of_calculate_amount_to_be_paid():
    try:
        _ = calculate_amount_to_be_paid(total_bill=1000, amount_deposited=100)
        assert True
    except (NameError, AssertionError):
        assert False


# Unit test
def test_calculate_amount_to_be_paid_with_invalid_arguments_type():
    with pytest.raises(ValueError):
        _ = calculate_amount_to_be_paid(total_bill='a', amount_deposited=[])
        assert False
    assert True


# Unit test
def test_calculate_amount_to_be_paid_with_valid_arguments_type():
    amount_payable = calculate_amount_to_be_paid(total_bill=1000, amount_deposited=200)
    assert amount_payable == 800


