from src.Product import Product


class Smartphone(Product):
    efficiency: str
    model: str
    ram: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price_t: float,
        quantity: int,
        efficiency: str,
        model: str,
        ram: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price_t, quantity)
        self.efficiency = efficiency
        self.model = model
        self.ram = ram
        self.color = color
