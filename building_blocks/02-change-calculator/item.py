class Item:

    def __init__(self, item_name: str, unit_price: float):
        """
        :param item_name: Name of the item
        :param unit_price: Unit price of the item
        """
        self.name = item_name
        self.price = unit_price

    @property
    def name(self) -> str:
        """
        :return: Item Name
        """
        return self._item_name

    @name.setter
    def name(self, item_name: str) -> None:
        """
        :param item_name: name of the item
        :return: None
        """
        if not isinstance(item_name, str):
            raise ValueError('Invalid Name')
        self._item_name = item_name

    @property
    def price(self) -> float:
        """
        :return: price of item
        """
        return self._unit_price

    @price.setter
    def price(self, unit_price: float) -> None:
        """
        :param unit_price: unit price of the item
        :return:
        """
        if not (isinstance(unit_price, float) or isinstance(unit_price, int)) or unit_price <= 0 :
            raise ValueError('Invalid price')
        self._unit_price = unit_price

