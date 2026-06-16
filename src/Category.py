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
        self.__products.append(added_product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        data = [f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт." for prod in self.__products]
        return "\n".join(data)
