import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture
def category() -> Category:
    return Category("Phones", "phone", [Product("IPhone", "phone", 1000, 5)])


@pytest.fixture
def category_2() -> Category:
    return Category("Laptops", "laptops", [Product("Acer", "laptop", 45647, 5), Product("Asus", "laptop", 45647, 5)])


@pytest.fixture
def product_1() -> Product:
    return Product("Samsung", "phone", 1000, 5)


@pytest.fixture
def product_2() -> Product:
    return Product("IPhone", "phone", 10000, 5)
