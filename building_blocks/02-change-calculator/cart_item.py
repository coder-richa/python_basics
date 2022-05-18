from item import Item


class CartItem:
    def __init__(self, new_item: Item, quantity: int):
        """
        :param new_item: Item purchased
        :param quantity: Number of items
        """
        self.item = new_item
        self.quantity = quantity

    @property
    def item(self) -> Item:
        """
        :return: Item purchased
        """
        return self._item

    @item.setter
    def item(self, new_item: Item) -> None:
        """
        :param new_item: Item to be added to cart
        :return:
        """
        if not isinstance(new_item, Item):
            raise ValueError("Invalid Item")
        self._item = new_item

    @property
    def quantity(self) -> int:
        """
        :return: quantity purchased
        """
        return self._quantity

    @quantity.setter
    def quantity(self, qty: int) -> None:
        if not isinstance(qty, int) or qty < 1:
            raise ValueError("Invalid quantity")
        self._quantity = qty

    def get_total(self) -> float:
        """
        :return: total amount chargeable for the given cart item
        """
        return self.item.price * self.quantity
