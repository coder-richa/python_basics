from cart import Cart


def calculate_change(cart: Cart, amount_paid: float):
    if not isinstance(cart, Cart):
        raise ValueError('Invalid cart reference')
    if not (isinstance(amount_paid, float) or  isinstance(amount_paid, int)) or amount_paid < 0:
        raise ValueError('Invalid amount paid')
    amount_chargeable = cart.get_total()
    return amount_paid - amount_chargeable
