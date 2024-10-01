from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone
from src.product import Product


class Category:
    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.product_count = len(products)
        Category.category_count += 1

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count} шт."

    def add_product(self, product):
        if issubclass(type(product), Product) or isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1

    @property
    def products(self):
        product_list = []
        for product in self.__products:
            product_list.append(str(product))
        return product_list
