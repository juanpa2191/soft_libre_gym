class Membership:
    def __init__(self, id=None, name=None, duration_months=None, price=None, description=None):
        self.id = id
        self.name = name
        self.duration_months = duration_months
        self.price = price
        self.description = description

    def __str__(self):
        return f"Membership(id={self.id}, name={self.name}, price={self.price})"