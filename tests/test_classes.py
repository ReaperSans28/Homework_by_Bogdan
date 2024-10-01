import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


@pytest.fixture
def product_iphone():
    return Product(
        "Iphone 17 blble", "256TB, цвет 'Звезды в шоке', 200GP камера", 18, 4
    )


@pytest.fixture
def category():
    return Category("Смартфоны", "Современные смартфоны", [1, 2, 3])


@pytest.fixture
def smartphone():
    return Smartphone(
        "Xiao",
        "Как Сяоми, но сейчас модно сокращать названия, поэтому Сяо",
        200,
        1,
        1.6,
        "мини",
        160,
        "Зеленый",
    )


@pytest.fixture
def lawn_grass():
    return LawnGrass(
        "GG",
        "GG - green grass",
        2000,
        300,
        "USA",
        "1 week",
        "Green"
    )


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


def test_fail_add(category, product_iphone):
    try:
        category.add_product(product_iphone)
    except Exception as e:
        assert type(e) is TypeError


def test_add_smartphone(category, smartphone):
    assert len(category.products) == 3
    assert type(category.products[0]) is str
    assert Category.product_count == 0


def test_str(category, product_iphone):
    assert str(product_iphone) == "Iphone 17 blble, 18 руб. Остаток: 4 шт."
    assert str(category) == "Смартфоны, количество продуктов: 3 шт."


def test_add(product_iphone):
    product = Product.new_product(
        {"name": "name1", "description": "-", "price": 140, "quantity": 3}
    )
    assert product_iphone + product == 442


def test_init3(smartphone):
    assert smartphone.name == "Xiao"
    assert smartphone.description == "Как Сяоми, но сейчас модно сокращать названия, поэтому Сяо"
    assert smartphone.price == 200
    assert smartphone.quantity == 1
    assert smartphone.efficiency == 1.6
    assert smartphone.model == "мини"
    assert smartphone.memory == 160
    assert smartphone.color == "Зеленый"


def test_init4(lawn_grass):
    assert lawn_grass.name == "GG"
    assert lawn_grass.description == "GG - green grass"
    assert lawn_grass.price == 2000
    assert lawn_grass.quantity == 300
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "1 week"
    assert lawn_grass.color == "Green"
