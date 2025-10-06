class Payment:
    def __init__(self, id=None, member_id=None, amount=None, paid_at=None, method=None, reference=None):
        self.id = id
        self.member_id = member_id
        self.amount = amount
        self.paid_at = paid_at
        self.method = method
        self.reference = reference

    def __str__(self):
        return f"Payment(id={self.id}, member_id={self.member_id}, amount={self.amount}, method={self.method})"