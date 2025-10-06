class Sale:
    def __init__(self, id=None, member_id=None, total=None, sale_date=None, created_by=None):
        self.id = id
        self.member_id = member_id
        self.total = total
        self.sale_date = sale_date
        self.created_by = created_by

    def __str__(self):
        return f"Sale(id={self.id}, member_id={self.member_id}, total={self.total})"