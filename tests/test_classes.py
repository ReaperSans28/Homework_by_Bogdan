import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def product_iphone():
    return Product("Iphone 17 blble", "256TB, цвет 'Звезды в шоке', 200GP камера", 0.18, 4)


def test_init1(product_iphone):
    assert product_iphone.name == "Iphone 17 blble"
    assert product_iphone.description == "256TB, цвет 'Звезды в шоке', 200GP камера"
    assert product_iphone.price == 0.18
    assert product_iphone.quantity == 4


@pytest.fixture
def category_iphone():
    return Category("Iphone", "Айфоны, многа", ["1", "2", "3"])


def test_init2(category_iphone):
    assert category_iphone.name == "Iphone"
    assert category_iphone.description == "Айфоны, многа"
    assert category_iphone.products == ["1", "2", "3"]
    assert category_iphone.product_count == 3
    assert category_iphone.category_count == 1
