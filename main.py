from src import Loader
from src.Category import Category
from src.Product import Product


def display_from_file() -> None:
    data = Loader.load_categories_from_file("./data/products.json")
    for category in data:
        print(f"Category: {category.name}\nDescription: {category.description}\nList of products:\n")
        print(category.products)
        print("****")


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
    print("***\nЗадание со *")
    for product in category1:
        print(product)