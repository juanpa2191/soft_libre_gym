class Product:
    def __init__(self, id=None, name=None, sku=None, price=None, supplier_id=None):
        self.id = id
        self.name = name
        self.sku = sku
        self.price = price
        self.supplier_id = supplier_id

    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, sku={self.sku}, price={self.price})"