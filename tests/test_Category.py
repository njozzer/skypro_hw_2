from src.Category import Category


def test_category(category: Category) -> None:
    assert category.name == "Phones"
    assert Category.product_count == 1
    assert Category.category_count == 1


def test_categories(category: Category, category_2: Category) -> None:
    assert category.name == "Phones"
    assert category_2.name == "Laptops"
    assert Category.product_count == 4
    assert Category.category_count == 3
