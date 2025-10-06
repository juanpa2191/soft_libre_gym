class Inventory:
    def __init__(self, product_id=None, quantity=None, min_quantity=None, last_updated=None):
        self.product_id = product_id
        self.quantity = quantity
        self.min_quantity = min_quantity
        self.last_updated = last_updated

    def __str__(self):
        return f"Inventory(product_id={self.product_id}, quantity={self.quantity}, min_quantity={self.min_quantity})"