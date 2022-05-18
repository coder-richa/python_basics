import functools


def calculate_total(values=[int]) -> int:
    """
    :param values: presents list of integers
    :return: sum of all values present in the list
    """
    if not isinstance(values, list) or not all(map(lambda a: isinstance(a, int), values)):
        raise ValueError("Invalid values")
    return functools.reduce(lambda a, b: a + b, values, 0)


def calculate_amount_to_be_paid(total_bill: int, amount_deposited: int = 0) -> int:
    """

    :param total_bill: Total price of the items purchased
    :param amount_deposited: Any previous deposit in the account
    :return: 0 in case the amount_deposited is greater than the total bill,
                otherwise return net amount payable
    """
    if not isinstance(total_bill, int) or not isinstance(amount_deposited, int):
        raise ValueError("Invalid values")

    # return 0 in case the amount_deposited is greater than the total bill
    if total_bill < amount_deposited:
        return 0
    # return net amount payable
    return total_bill - amount_deposited

