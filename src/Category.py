from src import Product


class Category:
    name: str
    description: str
    products: list[Product.Product]

    def __init__(self) -> None:
        pass
