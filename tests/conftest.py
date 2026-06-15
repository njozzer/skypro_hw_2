import pytest

from src.Category import Category
from src.Product import Product

@pytest.fixture
def category():
    return Category("","",[])

@pytest.fixture
def product_1():
    return Product("Samsung","phone",1000, 5)

@pytest.fixture
def product_2():
    return Product("IPhone", "phone", 10000, 5)