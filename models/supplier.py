class Supplier:
    def __init__(self, id=None, name=None, contact=None):
        self.id = id
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"Supplier(id={self.id}, name={self.name})"