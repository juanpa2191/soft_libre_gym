class Trainer:
    def __init__(self, id=None, first_name=None, last_name=None, email=None, phone=None, hire_date=None, specialty=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.hire_date = hire_date
        self.specialty = specialty

    def __str__(self):
        return f"Trainer(id={self.id}, name={self.first_name} {self.last_name}, specialty={self.specialty})"