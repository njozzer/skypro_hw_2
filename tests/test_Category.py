import pytest

from src.Category import Category
from src.Product import Product


def test_category(category: Category) -> None:
    assert category.name == "Phones"
    assert Category.product_count == 1
    assert Category.category_count == 1


def test_categories(category: Category, category_2: Category) -> None:
    assert category.name == "Phones"
    assert category_2.name == "Laptops"
    assert Category.product_count == 4
    assert Category.category_count == 3


def test_add_product(category: Category) -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_count = category.product_count
    category.add_product(product1)
    assert category.product_count == product_count + 1


def test_category_products_property(category: Category) -> None:
    assert category.products == "IPhone, 1000 руб. Остаток: 5 шт."


def test_category_str(category: Category) -> None:
    assert category.__str__() == "Phones, количество продуктов: 5 шт."

def test_category_iter() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    category1_iter = category1.__iter__()
    assert category1_iter.__next__() == product1
    assert category1_iter.__next__() == product2
    assert category1_iter.__next__() == product3
    with pytest.raises(StopIteration):
        category1_iter.__next__()