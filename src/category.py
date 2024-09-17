class Category:
    name: str
    description: str
    products: str
    product_count: int
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.product_count = len(products)
        Category.category_count += 1
