class Role:
    def __init__(self, id=None, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        return f"Role(id={self.id}, name={self.name})"