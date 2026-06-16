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
