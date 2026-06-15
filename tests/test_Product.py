from src.Product import Product


def test_product(product_1: Product) -> None:
    assert product_1.name == "Samsung"
    assert product_1.price == 1000
