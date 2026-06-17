from typing import Self

from src.BaseProduct import BaseProduct
from src.MixinLog import MixinLog


class Product(BaseProduct, MixinLog):

    __price: float = 0.0

    def __init__(self, name: str, description: str, price_t: float, quantity: int) -> None:

        self.name = name
        self.description = description
        self.__price = price_t
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.quantity = quantity
        MixinLog.__init__(self)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price_2: float) -> None:
        if price_2 <= 0.0:
            print("Ошибка: Цена должна быть больше 0")
        else:
            if self.__price > price_2:
                while True:
                    result = str(
                        input("Изменить цену на меньшую?[y/n]")
                    )  # input в сеттере не работает ?!!! зачем задание такое?
                    if result.lower() == "y":
                        self.__price = price_2
                        break
                    elif result.lower() == "n":
                        break
                    else:
                        print("Можно вводить только [y/n]")
            else:
                self.__price = price_2

    @classmethod
    def new_product(cls, product_dict: dict, product_list: list[Self] = []) -> Self:
        if product_list is not None:
            for product in product_list:
                if str(product_dict.get("name", "name")) == product.name:
                    product.quantity += product_dict.get("quantity", 0)
                    product.price = (
                        product.price if product_dict.get("price", 0) < product.price else product_dict.get("price", 0)
                    )
                    return product

        return cls(
            str(product_dict.get("name", "")),
            str(product_dict.get("description", "")),
            float(product_dict.get("price", 0.0)),
            int(product_dict.get("quantity", 0)),
        )

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: object) -> float:
        if not isinstance(other, Product):
            return NotImplemented
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать продукты разных типов")
        else:
            return self.quantity * self.price + other.quantity * other.price
