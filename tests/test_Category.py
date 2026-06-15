from src.Category import Category


def test_category(category: Category) -> None:
    assert category.name == "Phones"
    assert category.product_count == 1
    assert category.category_count == 1
