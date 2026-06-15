import pytest

from src.Product import Product


def test_product(product_1):
    assert product_1().name == "Samsung"
    assert product_1().price == 1000

