import pytest

from src.Category import Category
from src.Product import Product

@pytest.fixture
def category():
    return Category("","",[])

@pytest.fixture
def product():
    return Product("Samsung","phone",1000)