from cart import Cart
from item import Item
from cart_item import CartItem
from change_calculator import calculate_change

cartons_item = Item("Milk Carton", 2.5)
mars_bar_item = Item("Mars Bar", 1.2)
indigestion_tablets_pack_item = Item("Indigestion Tablets Pack", 3.5)
cart = Cart()
cart.add(item=CartItem(new_item=cartons_item, quantity=2))
cart.add(item=CartItem(new_item=mars_bar_item, quantity=5))
cart.add(item=CartItem(new_item=indigestion_tablets_pack_item, quantity=1))

amount_paid = 20
change = calculate_change(cart=cart, amount_paid=amount_paid)
print(change)