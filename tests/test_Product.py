from src.Product import Product
from unittest.mock import mock_open, patch, PropertyMock

def test_product(product_1: Product) -> None:
    assert product_1.name == "Samsung"
    assert product_1.price == 1000


def test_product_2() -> None:
    product_test = Product("Samsung", "description", 1000, 5)
    assert product_test.name == "Samsung"
    assert product_test.price == 1000
    product_test.price = 2000
    assert product_test.price == 2000



def test_product_3() -> None:
    product_test = Product("Samsung", "description", 1000, 5)
    assert product_test.name == "Samsung"
    assert product_test.price == 1000
    product_test.price = -100
    assert product_test.price == 1000

def test_product_4_y() -> None:
    with patch("builtins.input", return_value="y") as mock_input:
        product_test = Product("Samsung", "description", 1000, 5)
        assert product_test.name == "Samsung"
        assert product_test.price == 1000
        product_test.price = 500
        assert product_test.price == 500
        assert mock_input.call_count == 1

def test_product_4_n() -> None:
    with patch("builtins.input", return_value="n") as mock_input:
        product_test = Product("Samsung", "description", 1000, 5)
        assert product_test.name == "Samsung"
        assert product_test.price == 1000
        product_test.price = 500
        assert product_test.price == 1000
        mock_input.assert_called_once_with("Изменить цену на меньшую?[y/n]")

def test_product_4_z() -> None:
    with patch.object(Product, 'price', new_callable=PropertyMock) as mock_prop:
        obj = Product("Samsung", "description", 1000, 5)
        obj.price = 500
        mock_prop.assert_called_once_with(500)


def test_product_new_product() -> None:
    product_test = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 10,
        }
    )

    assert product_test.name == "Samsung Galaxy S23 Ultra"
    assert product_test.price == 180000.0


def test_product_new_product_with_list() -> None:

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product_test = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 120000.0,
            "quantity": 20,
        },
        [product1, product2, product3],
    )
    assert product_test.name == "Samsung Galaxy S23 Ultra"
    assert product_test.price == 180000.0
    assert product_test.quantity == 25
