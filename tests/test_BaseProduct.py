from typing import Self

import pytest

from src.BaseProduct import BaseProduct


class DummyProduct(BaseProduct):

    def __str__(self) -> str:
        return "Dummy Product"

    def __add__(self, other: Self) -> float:
        return self.quantity + other.quantity

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


def test_base_product() -> None:
    dummy = DummyProduct("Dummy Product", "description", 1000, 5)
    assert dummy.name == "Dummy Product"


def test_base_product_instance() -> None:
    with pytest.raises(TypeError):
        BaseProduct("Dummy Product", "description", 1000, 5)  # type: ignore[abstract]
