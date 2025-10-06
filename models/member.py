class Member:
    def __init__(self, id=None, first_name=None, last_name=None, email=None, phone=None, birth_date=None, created_at=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.birth_date = birth_date
        self.created_at = created_at

    def __str__(self):
        return f"Member(id={self.id}, name={self.first_name} {self.last_name}, email={self.email})"