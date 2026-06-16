from typing import Self


class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price_2: float) -> None:
        if price_2 <= 0.0:
            print("Ошибка: Цена должна быть больше 0")
        else:
            if self.__price < price_2:
                result = str(
                    input("Изменить цену на меньшую?[y/n]")
                )  # input в сеттере не работает ?!!! зачем задание такое?
                if result.lower() == "y":
                    self.__price = price_2
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
