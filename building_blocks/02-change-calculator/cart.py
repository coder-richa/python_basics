from cart_item import CartItem


class Cart:

    def __init__(self):
        # Initialises empty cart
        self.items = []

    @property
    def items(self) -> [CartItem]:
        """
        :return: Items of the cart
        """
        return self._items

    @items.setter
    def items(self, items: [CartItem]) -> None:
        """
        :param items: Items of the cart
        :return:
        """
        self._items = items

    def add(self, item: CartItem) -> None:
        """
        :param item: Cart Item to be appended in the cart
        :return:
        """
        if not isinstance(item, CartItem):
            raise ValueError("Invalid item")
        self.items.append(item)

    def get_total(self) -> float:
        """
        :return: Total chargeable amount of the cart items
        """
        cart_total = 0
        for item in self.items:
            cart_total += item.get_total()
        return cart_total

    def items_count(self) -> int:
        """
        :return: Number of cart items
        """
        return len(self.items)
