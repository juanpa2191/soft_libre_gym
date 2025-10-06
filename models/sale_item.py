class SaleItem:
    def __init__(self, id=None, sale_id=None, product_id=None, quantity=None, price=None):
        self.id = id
        self.sale_id = sale_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"SaleItem(id={self.id}, sale_id={self.sale_id}, product_id={self.product_id}, quantity={self.quantity})"