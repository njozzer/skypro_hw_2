from src.Product import Product


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price_t: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price_t, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
