class User:
    def __init__(self, id=None, username=None, password_hash=None, role_id=None, full_name=None, email=None, created_at=None):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.role_id = role_id
        self.full_name = full_name
        self.email = email
        self.created_at = created_at

    def __str__(self):
        return f"User(id={self.id}, username={self.username}, full_name={self.full_name})"