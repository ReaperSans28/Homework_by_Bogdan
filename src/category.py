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
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1

    @property
    def products(self):
        product_list = []
        for product in self.__products:
            product_list.append(str(product))
        return product_list

    def average_price(self):
        try:
            if not self.__products:
                raise ValueError("Категория не содержит товаров.")
            total_price = sum(product.price * product.quantity for product in self.__products)
            total_quantity = sum(product.quantity for product in self.__products)
            if total_quantity == 0:
                return 0
            return total_price / total_quantity
        except ZeroDivisionError:
            return 0
        except ValueError as e:
            print(e)
            return 0
