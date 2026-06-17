from typing import Iterator

from src.Product import Product


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, added_product: Product) -> None:
        if not isinstance(added_product, Product):
            raise TypeError
        self.__products.append(added_product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        data = [f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт." for prod in self.__products]
        return "\n".join(data)

    def __str__(self) -> str:
        count_list = [item.quantity for item in self.__products]
        quantity = sum(count_list)
        return f"{self.name}, количество продуктов: {quantity} шт."

    def __iter__(self) -> Iterator[Product]:
        """Возвращает итератор."""
        self.current_value = -1
        return self

    def __next__(self) -> Product:
        if self.current_value + 1 < len(self.__products):
            self.current_value += 1
            return self.__products[self.current_value]
        else:
            raise StopIteration

    def middle_price(self) -> float:
        try:
            avg_price = sum([product.price for product in self.__products]) / sum(
                [product.quantity for product in self.__products]
            )
            return avg_price
        except Exception:
            return 0.0
