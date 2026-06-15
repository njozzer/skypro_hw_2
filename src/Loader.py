from typing import List

from src.Category import Category
from src.Product import Product
from src.utils import json_read_from_file


def load_categories_from_file(file_name: str) -> List[Category]:  # pragma: no cover
    categories = json_read_from_file(file_name)
    categories_list: List[Category] = []
    for category in categories:
        product_list: List[Product] = []
        for product in category.get("products", {}):
            product = Product(
                str(product.get("name", "")),
                str(product.get("description", "")),
                float(product.get("price", 0.0)),
                int(product.get("quantity", 0)),
            )
            product_list.append(product)
        category_to_list: Category = Category(
            str(category.get("name", "")), str(category.get("description")), product_list
        )
        categories_list.append(category_to_list)

    return categories_list
