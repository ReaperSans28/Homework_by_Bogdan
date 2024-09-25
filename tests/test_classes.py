import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_iphone():
    return Product(
        "Iphone 17 blble", "256TB, цвет 'Звезды в шоке', 200GP камера", 18, 4
    )


@pytest.fixture
def category():
    return Category("Смартфоны", "Современные смартфоны", [1, 2, 3])


def test_init1(product_iphone):
    assert product_iphone.name == "Iphone 17 blble"
    assert product_iphone.description == "256TB, цвет 'Звезды в шоке', 200GP камера"
    assert product_iphone.price == 18
    assert product_iphone.quantity == 4


def test_set_price_positive(product_iphone):
    product_iphone.price = 0.25
    assert product_iphone.price == 0.25


def test_set_price_zero_or_negative(product_iphone):
    product_iphone.price = -5
    assert product_iphone.price == 18
    product_iphone.price = 0
    assert product_iphone.price == 18


def test_add_product_to_category(category, product_iphone):
    category.add_product(product_iphone)
    assert len(category.products) == 4
    assert type(category.products[0]) is str


def test_category_product_count(category, product_iphone):
    category.add_product(product_iphone)
    assert Category.product_count == 2


def test_str(category, product_iphone):
    assert str(product_iphone) == "Iphone 17 blble, 18 руб. Остаток: 4 шт."
    assert str(category) == "Смартфоны, количество продуктов: 3 шт."


def test_add(product_iphone):
    product = Product.new_product({"name": "name1", "description": "-", "price": 140, "quantity": 3})
    assert product_iphone + product == 442
