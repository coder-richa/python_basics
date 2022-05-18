import pytest
from item import Item
from cart_item import CartItem
from cart import Cart
from change_calculator import calculate_change


# Unit test
def test_accessibility_of_item():
    try:
        _ = Item('Item name', 10)
        assert True
    except (NameError, AssertionError):
        assert False


# Unit test
def test_creating_item_with_invalid_name():
    with pytest.raises(ValueError):
        _ = Item(item_name=10, unit_price=10)
        assert False
    assert True


# Unit test
def test_creating_item_with_invalid_price():
    with pytest.raises(ValueError):
        _ = Item(item_name="Item name", unit_price=0)
        assert False
    assert True


# Unit test
def test_creating_item_with_valid_arguments():
    item = Item(item_name="Item name", unit_price=10)
    assert item.name == "Item name" and item.price == 10


# Unit test
def test_accessibility_of_cartitem():
    try:
        item = Item('Item name', 10)
        _ = CartItem(new_item=item, quantity=2)
        assert True
    except (NameError, AssertionError):
        assert False


# Unit test
def test_creating_cartitem_with_invalid_item():
    with pytest.raises(ValueError):
        _ = CartItem(new_item=[], quantity=2)
        assert False
    assert True


# Unit test
def test_creating_cartitem_with_invalid_quantity():
    with pytest.raises(ValueError):
        item = Item('Item name', 10)
        _ = CartItem(new_item=item, quantity=0)
        assert False
    assert True


# Unit test
def test_creating_cartitem_with_valid_argument():
    item = Item('Item name', 10)
    cart = CartItem(new_item=item, quantity=10)
    assert cart.item == item and cart.quantity == 10


# Unit test
def test_cart_item_total_price():
    item = Item('Item name', 10)
    cart = CartItem(new_item=item, quantity=2)
    assert cart.get_total() == 20


# Unit test
def test_accessibility_of_cart():
    try:
        _ = Cart()
        assert True
    except (NameError, AssertionError):
        assert False


# Unit test
def test_initial_cart_items():
    cart = Cart()
    assert cart.items_count() == 0


# Unit test
def test_add_invalid_item_to_cart():
    with pytest.raises(ValueError):
        cart = Cart()
        cart.add([])
        assert False
    assert True


# Unit test
def test_add_valid_item_to_cart():
    cart = Cart()
    item = Item('Item name', 10)
    cart_item = CartItem(new_item=item, quantity=2)
    cart.add(cart_item)
    assert cart.items_count() == 1


# Unit test
def test_cart_total():
    cart = Cart()
    item = Item('Item name', 10)
    item2 = Item('Item name', 100)
    cart_item = CartItem(new_item=item, quantity=2)
    cart_item2 = CartItem(new_item=item2, quantity=1)
    cart.add(cart_item)
    cart.add(cart_item2)
    assert cart.get_total() == 120


# Unit test
def test_accessibility_of_calculate_change():
    try:
        _ = calculate_change(cart=Cart(), amount_paid=10)
        assert True
    except (NameError, AssertionError):
        assert False


# Unit test
def test_invalid_cart_argument_of_calculate_change():
    with pytest.raises(ValueError):
        _ = calculate_change(cart=[], amount_paid=10)
        assert False
    assert True


# Unit test
def test_invalid_amount_paid_argument_of_calculate_change():
    with pytest.raises(ValueError):
        _ = calculate_change(cart=[], amount_paid=-1)
        assert False
    assert True


# Unit test
def test_calculate_change_result():
    cartons_item = Item("Milk Carton", 2.5)
    mars_bar_item = Item("Mars Bar", 1.2)
    indigestion_tablets_pack_item = Item("Indigestion Tablets Pack", 3.5)
    cart = Cart()
    cart.add(item=CartItem(new_item=cartons_item, quantity=2))
    cart.add(item=CartItem(new_item=mars_bar_item, quantity=5))
    cart.add(item=CartItem(new_item=indigestion_tablets_pack_item, quantity=1))
    amount_paid = 20
    change = calculate_change(cart=cart, amount_paid=amount_paid)
    assert change == 5.5